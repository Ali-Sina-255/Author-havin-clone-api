from uuid import UUID

from django.db import IntegrityError
from rest_framework import generics, permissions
from rest_framework.exceptions import NotFound, ValidationError

from apps.articles.models import Article

from .models import Bookmark
from .serializers import BookmarkSerializer


class BookmarkCreateView(generics.CreateAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        article_id = self.kwargs["article_id"]
        if article_id:
            try:
                article = Article.objects.get(id=article_id)
            except Article.DoesNotExist:
                raise ValidationError("Invalid article id is provided")

        else:
            raise ValidationError("article id is required.")
        try:
            serializer.save(user=self.request.user, article=article)
        except IntegrityError:
            raise ValidationError("you have already bookmarked this article.")


class BookmarkDestroyView(generics.DestroyAPIView):
    queryset = Bookmark.objects.all()
    lookup_field = "article_id"
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        user = self.queryset.user
        article_id = self.kwargs.get("article_id")

        try:
            UUID(str(article_id), version=4)
        except ValueError:
            raise ValidationError("Invalid article id provided")
        try:
            bookmark = Bookmark.objects.create(user=user, article_id=article_id)
        except Bookmark.DoesNotExist:
            raise NotFound('Bookmark not found or it doesn"t belong to you.')

        return bookmark

    def perform_destroy(self, instance):
        user = self.request.user

        if instance.user != user:
            raise ValidationError("you cannot delete a bookmark that is not yours")
        instance.delete()

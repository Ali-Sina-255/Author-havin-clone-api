import logging

from django.contrib.auth import get_user_model
from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, permissions, status
from rest_framework.response import Response

from .filters import ArticleFilter
from .models import Article, ArticleView
from .pagination import ArticlePagination
from .permissions import IsOwnerOrReadOnly
from .renderers import ArticleJSONRenderer, ArticlesJSONRenderer
from .serializers import ArticleSerializer

User = get_user_model()

logger = logging.getLogger(__name__)


class ArticleListCreateViewSet(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [ArticlesJSONRenderer]
    pagination_class = ArticlePagination
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_class = ArticleFilter
    ordering_fields = ["created_at", "updated_at"]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        logger.info(
            f"article {serializer.data.get('title')} created by {self.request.user.first_name}"
        )


class ArticleRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    lookup_field = "id"
    renderer_classes = [ArticleJSONRenderer]

    def perform_update(self, serializer):
        # Ensure the author is updated correctly
        serializer.save(author=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except Http404:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(instance)
        viewer_ip = request.META.get("REMOTE_ADDR", None)
        ArticleView.record_view(
            article=instance, viewer_ip=viewer_ip, user=request.user
        )

        return Response(serializer.data)

from django.urls import path

from . import views

urlpatterns = [
    path(
        "bookmarks_article/<uuid:article_id>/",
        views.BookmarkCreateView.as_view(),
        name="bookmark_article",
    ),
    path(
        "remove_bookmark/<uuid:article_id>/",
        views.BookmarkDestroyView.as_view(),
        name="remove_bookmark",
    ),
]

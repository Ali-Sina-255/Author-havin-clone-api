from django.urls import path

from . import views

urlpatterns = [
    path("", views.ArticleListCreateViewSet.as_view(), name="article-list-create"),
    path(
        "<uuid:id>/",
        views.ArticleRetrieveUpdateDestroyView.as_view(),
        name="article-retrieve-update-destroy",
    ),
    path('<uuid:article_id>/clap/',views.ClapArticleView.as_view(),name='clap-article')
]

from django.urls import path

from . import views

urlpatterns = [
    path(
        "search/",
        views.ArticleElasticSearchView.as_view({"get": "list"}),
        nam="article-search",
    )
]

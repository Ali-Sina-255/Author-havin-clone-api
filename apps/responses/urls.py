from django.urls import path

from . import views

urlpatterns = [
    path(
        "article/<uuid:article_id>/",
        views.ResponseView.as_view(),
        name="article_response",
    ),
    path(
        "<uuid:id>/", views.ResponseUpdateDestroyView.as_view(), name="response_details"
    ),
]

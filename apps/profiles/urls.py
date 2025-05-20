from django.urls import path

from . import views

urlpatterns = [
    path("all/", views.ProfileListAPIView.as_view(), name="all-profiles"),
    path("me/", views.ProfileDetailAPIView.as_view(), name="my-profile"),
    path("me/update/", views.UpdateProfileAPIView.as_view(), name="update-profile"),
    path("me/followers/", views.FollowerListView.as_view(), name="followers"),
    path(
        "<uuid:user_id>/follow/",
        views.FollowAPIView.as_view(),
        name="follow",
    ),
    path(
        "<uuid:user_id>/unfollow/",
        views.unFollowAPIView.as_view(),
        name="unfollow",
    ),
]

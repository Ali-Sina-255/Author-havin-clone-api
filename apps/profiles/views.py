from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from rest_framework import generics, status
from rest_framework.exceptions import NotFound
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from config.settings.local import DEFAULT_FROM_EMAIL

from .exceptions import CantFollowYourSelf
from .models import Profile
from .pagination import ProfilePagination
from .renderers import ProfileJsonRenderers, ProfilesJsonRenderers
from .serializers import (
    FollowingSerializer,
    ProfileSerializers,
    UpdateProfileSerializer,
)

User = get_user_model()


class ProfileListAPIView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializers
    permission_classes = [IsAuthenticated]
    pagination_class = ProfilePagination
    renderer_classes = [ProfilesJsonRenderers]


class ProfileDetailAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializers
    renderer_classes = [ProfileJsonRenderers]

    def get_queryset(self):
        queryset = Profile.objects.select_related("user")
        return queryset

    def get_object(self):
        user = self.request.user
        profile = self.get_queryset().get(user=user)
        return profile


class UpdateProfileAPIView(generics.UpdateAPIView):
    serializer_class = ProfileSerializers
    pagination_class = [ProfilePagination]
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser]
    renderer_classes = [ProfileJsonRenderers]

    def get_object(self):
        profile = self.request.user.profile
        return profile

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class FollowerListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        try:
            profile = Profile.objects.get(user__id=request.user.id)
            follower_profiles = profile.followers.all()
            serializer = FollowingSerializer(follower_profiles, many=True)
            formatted_response = {
                "status_code": status.HTTP_200_OK,
                "followers_count": follower_profiles.count(),
                "followers": serializer.data,
            }
            return Response(formatted_response, status=status.HTTP_200_OK)
        except Profile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class FollowingListView(APIView):

    def get(self, request, user_id, format=None):
        try:
            profile = Profile.objects.get(user__id=user_id)
            following_profiles = profile.following.all()
            users = [p.user for p in following_profiles]
            serializer = FollowingSerializer(users, many=True)

            formatted_response = {
                "status_code": status.HTTP_200_OK,
                "followers_count": following_profiles.count(),
                "followers": serializer.data,
            }
            return Response(formatted_response, status=status.HTTP_200_OK)
        except Profile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class FollowAPIView(APIView):
    def post(self, request, user_id, format=None):
        try:
            follower = Profile.objects.get(user=self.request.user)
            user_profile = request.user.profile
            profile = Profile.objects.get(user__id=user_id)
            if profile == follower:
                raise CantFollowYourSelf
            if user_profile.check_following(profile):

                formatted_response = {
                    "status_code": status.HTTP_400_BAD_REQUEST,
                    "message": f"you are already following {profile.user.first_name} {profile.user.last_name}",
                }
                return Response(formatted_response, status=status.HTTP_400_BAD_REQUEST)
            user_profile.follow(profile)
            subject = "A new User follows you."
            message = f"Hi there. {profile.user.first_name}!!, the user {profile.user.first_name} {profile.user.last_name} now follows you"
            from_email = DEFAULT_FROM_EMAIL
            recipients_list = [profile.user.email]
            send_mail(subject, message, from_email, recipients_list, fail_silently=True)
            formatted_response = {
                "status_code": status.HTTP_200_OK,
                "message": f"you are now following {profile.user.first_name} {profile.user.last_name}",
            }
            return Response(formatted_response)
        except Profile.DoesNotExist:
            raise NotFound("you can't follow a profile that does not exist.")


class unFollowAPIView(APIView):
    def post(self, request, user_id, format=None):
        user_profile = request.user.profile
        profile = Profile.objects.get(user__id=user_id)
        if not user_profile.check_following(profile):
            formatted_response = {
                "status_code": status.HTTP_400_BAD_REQUEST,
                "message": f"you can't unfollow {profile.user.first_name} {profile.user.last_name}, since you were not following then in the first place.",
            }
            return Response(formatted_response, status=status.HTTP_400_BAD_REQUEST)
        user_profile.unfollow(profile)
        formatted_response = {
            "status_code": status.HTTP_200_OK,
            "message": f"you have unfollowed {profile.user.first_name} {profile.user.last_name}.",
        }
        return Response(formatted_response, status=status.HTTP_200_OK)

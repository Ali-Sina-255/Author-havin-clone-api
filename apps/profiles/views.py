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

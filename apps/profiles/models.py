from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

from apps.common.models import TimeStampedModel

User = get_user_model()


class Profile(TimeStampedModel):
    class GENDER(models.TextChoices):
        MALE = "M", _("Male")
        FEMALE = "F", _("FEMALE")
        OTHER = "O", _("Other")

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    phone_number = PhoneNumberField(
        verbose_name=_("Phone Number "), max_length=30, default="+93707323964"
    )
    about_me = models.TextField(
        verbose_name=_("about me"), default="say something about your self."
    )

    gender = models.CharField(
        verbose_name=_("gender"),
        choices=GENDER.choices,
        default=GENDER.MALE,
        max_length=2,
    )
    country = CountryField(
        verbose_name=_("country"), default="Af", blank=True, null=True
    )
    city = models.CharField(
        verbose_name=_("city"), max_length=255, default="Kabul", blank=True, null=True
    )
    profile_photo = models.ImageField(
        verbose_name=_("profile photo"), default="/profile_default.png"
    )
    twitter_handle = models.CharField(
        verbose_name=_("twitter handle"), max_length=20, blank=True, null=True
    )
    followers = models.ManyToManyField(
        "self",
        symmetrical=False,
        related_name="following",
        blank=True,
    )

    def __str__(self):
        return f'{self.user.first_name}"s Profile'

    def follow(self, profile):
        set.followers.add(profile)

    def unfollow(self, profile):
        self.followers.remove(profile)

    def check_following(self, profile):
        return self.followers.filter(pkid=profile.pkid).exists()
    
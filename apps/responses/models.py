from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy

from apps.articles.models import Article
from apps.common.models import TimeStampedModel

User = get_user_model()


class Response(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="responses")
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="responses",
        blank=True,
        null=True,
    )
    parent_response = models.ForeignKey(
        "self", on_delete=models.CASCADE, related_name="replies", null=True, blank=True
    )
    content = models.TextField(verbose_name="response content")

    class Meta:
        verbose_name = "Response"
        verbose_name_plural = "Responses"
        ordering = ["created_at"]

    def __str__(self):
        return f"{self.user.first_name} commented on {self.article.title}"

from django.contrib.auth import get_user_model
from django.db import models

from apps.articles.models import Article
from apps.common.models import TimeStampedModel

User = get_user_model()


class Rating(TimeStampedModel):
    RATING_CHOICES = [
        (1, "Poor"),
        (2, "Fair"),
        (3, "Good"),
        (4, "Very Good"),
        (5, "Excellent"),
    ]

    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="ratings"
    )
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField(blank=True)

    class Meta:
        verbose_name = "Rating"
        verbose_name_plural = "Rating"
        unique_together = ("article", "user")

    def __str__(self):
        return f"{self.user.first_name} rated {self.article.title} as {self.get_rating_display()}"

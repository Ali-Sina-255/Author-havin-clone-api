from django.contrib import admin

from .models import Response


class AdminResponse(admin.ModelAdmin):
    list_display = [
        "pkid",
        "id",
        "user",
        "article",
        "parent_response",
        "content",
        "created_at",
    ]
    list_display_links = ["id", "user", "article"]


admin.site.register(Response, AdminResponse)

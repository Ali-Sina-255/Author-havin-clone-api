from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django_elasticsearch_dsl.registries import registry

from apps.articles.models import Article


@receiver(post_save, sender=Article)
def update_document(sender, instance, **kwargs):
    registry.update(instance)


@receiver(post_delete, sender=Article)
def delete_document(sender, instance, **kwargs):
    registry.delete(instance)

from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from .documents import ArticleDocuments


class ArticleElasticSearchSerializer(DocumentSerializer):
    class Meta:
        document = ArticleDocuments
        fields = ["title", "author", "slug", "description", "body", "created_at"]

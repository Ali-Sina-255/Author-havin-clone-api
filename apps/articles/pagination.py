from rest_framework.pagination import PageNumberPagination


class ArticlePagination(PageNumberPagination):
    page_size = 10
    max_page_size = 30
    page_size_query_param = "page_size"

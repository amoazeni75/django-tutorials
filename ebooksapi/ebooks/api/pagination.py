from rest_framework.pagination import PageNumberPagination


class SmallSizePagination(PageNumberPagination):
    page_size = 2

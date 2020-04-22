from django.urls import path
from ebooks.api.views import EbookListCreateAPIView

urlpatterns = [
    path('path', EbookListCreateAPIView.as_view(), 'ebooks-list')
]

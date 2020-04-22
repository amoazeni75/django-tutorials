from django.urls import path
from ebooks.api.views import EookListCreateAPIViewAdvanced

urlpatterns = [
    # path('ebooks/', EbookListCreateAPIView.as_view(), name='ebooks-list')
    path('ebooks/', EookListCreateAPIViewAdvanced.as_view(), name='ebooks-list')
]

from django.urls import path
from ebooks.api.views import (EookListCreateAPIViewAdvanced, EbookDetailAPIView,
                              ReviewCreateAPIView, ReviewDetailAPIView)

urlpatterns = [
    # path('ebooks/', EbookListCreateAPIView.as_view(), name='ebooks-list')
    path('ebooks/',
         EookListCreateAPIViewAdvanced.as_view(),
         name='ebooks-list'),

    path('ebooks/<int:pk>',
         EbookDetailAPIView.as_view(),
         name='ebooks-detail'),

    path('ebooks/<int:ebook_pk>/review',
         ReviewCreateAPIView.as_view(),
         name='ebooks-review'),

    path('review/<int:pk>',
         ReviewDetailAPIView.as_view(),
         name='review-detail'),
]

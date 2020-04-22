from django.urls import path
from quote.api.views import QuoteDetailAPIView, QuoteListCreateAPIView

urlpatterns = [
    path('quotes/', QuoteListCreateAPIView.as_view(), name='quotes-list'),
    path('quote/<int:pk>', QuoteDetailAPIView.as_view(), name='quotes-detail'),
]

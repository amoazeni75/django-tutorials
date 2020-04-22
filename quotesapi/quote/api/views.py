from rest_framework import generics
from quote.models import Quote
from quote.api.serializers import QuoteSerializer
from quote.api.permissions import IsAdminUserOrReadOnly
from quote.api.pagination import SmallPagination


class QuoteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Quote.objects.all().order_by("id")
    serializer_class = QuoteSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = SmallPagination


class QuoteDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [IsAdminUserOrReadOnly]

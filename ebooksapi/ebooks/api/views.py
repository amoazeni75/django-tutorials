from rest_framework import generics
from rest_framework.generics import get_object_or_404

from ebooks.models import Ebook, Review
from ebooks.api.serializers import EbookSerializer, ReviewSerializer

from rest_framework import permissions
from ebooks.api.permissions import IsAdminUserOrReadOnly, IsReviewAuthorOrReadOnly

from rest_framework.exceptions import ValidationError

from ebooks.api.pagination import SmallSizePagination

"""
In the following class we need to implement get, post method 
"""

# class EbookListCreateAPIView(mixins.ListModelMixin,
#                              mixins.CreateModelMixin,
#                              generics.GenericAPIView):
#     # 1: we should define two bellow things
#     queryset = Ebook.objects.all()
#     serializer_class = EbookSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


""" 
The following classes is same as the above class, but it has more ready-to-use codes
"""


class EookListCreateAPIViewAdvanced(generics.ListCreateAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer
    permission_classes = [IsAdminUserOrReadOnly]  # we implemented the class in the permissions.py
    pagination_class = SmallSizePagination


class EbookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    """
    we must override the following method, because it is for a general usage
    and we need to specify the ebook foreign key before serializer.save()
    """

    def perform_create(self, serializer):
        ebook_pk = self.kwargs["ebook_pk"]
        ebook = get_object_or_404(Ebook, pk=ebook_pk)
        review_author = self.request.user

        review_queryset = Review.objects.filter(ebook=ebook, review_author=review_author)
        if review_queryset.exists():
            raise ValidationError("Each user can only review once for each book")

        serializer.save(ebook=ebook, review_author=review_author)


class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewAuthorOrReadOnly]

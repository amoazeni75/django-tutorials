from rest_framework import viewsets
from questions.api.serializers import QuestionSerializer, AnswerSerializer
from questions.models import Question, Answer

from questions.api.permissions import IsAuthorOrReadOnly
from rest_framework.permissions import IsAuthenticated


class QuestionViewSet(viewsets.ModelViewSet):  # provide CRUD functionality
    queryset = Question.objects.all()
    lookup_field = "slug"
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

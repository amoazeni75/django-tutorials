from django.urls import path, include
from rest_framework.routers import DefaultRouter

from questions.api import views as qv

router = DefaultRouter()
router.register(r"questions", qv.QuestionViewSet)  # automatically support all urls related to question

urlpatterns = [
    path("", include(router.urls)),

    path("questions/<slug:slug>/answer/",
         qv.AnswerCreateAPIView.as_view(),
         name="answer-create"),

    path("questions/<slug:slug>/answers/",
         qv.QuestionAnswerListAPIView.as_view(),
         name="answers-list"),

    path("answers/<int:pk>/",
         qv.AnswerRUDAPIView.as_view(),
         name="answers-detail"),

    path("answers/<int:pk>/like/",
         qv.AnswerLikeAPIView.as_view(),
         name="answers-like")
]

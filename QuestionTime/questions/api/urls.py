from django.urls import path, include
from rest_framework.routers import DefaultRouter

from questions.api import views as qv

router = DefaultRouter()
router.register(r"questions", qv.QuestionViewSet)  # automatically support all urls related to question

urlpatterns = [
    path("", include(router.urls))
]

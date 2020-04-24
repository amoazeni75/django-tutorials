from django.urls import include, path
from profiles.api.views import ProfileViewSet
from rest_framework.routers import DefaultRouter

profile_list = ProfileViewSet.as_view({"get": "list"})
profile_detail = ProfileViewSet.as_view({"get": "retrieve"})

router = DefaultRouter()
router.register(r"profiles", ProfileViewSet)

urlpatterns = [
    # path('profiles/', ProfileList.as_view(), name='profiles-list'),

    # path('profiles/', profile_list, name='profiles-list'),
    # path('profile/<int:pk>/', profile_detail, name='profile-detail'),

    path("", include(router.urls)),
]

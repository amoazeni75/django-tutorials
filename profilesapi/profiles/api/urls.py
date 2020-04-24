from django.urls import path
from profiles.api.views import ProfileViewSet

profile_list = ProfileViewSet.as_view({"get": "list"})
profile_detail = ProfileViewSet.as_view({"get": "retrieve"})

urlpatterns = [
    # path('profiles/', ProfileList.as_view(), name='profiles-list'),
    path('profiles/', profile_list, name='profiles-list'),
    path('profile/<int:pk>/', profile_detail, name='profile-detail'),
]

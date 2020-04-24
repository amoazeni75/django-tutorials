from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from profiles.models import Profile, ProfileStatus
from profiles.api.serializers import ProfileSerializer, ProfileStatusSerializer, ProfileAvatarSerializer

# from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from rest_framework import mixins

from profiles.api.permissions import IsOwnProfileOrReadOnly, IsOwnerOrReadOnly

from rest_framework.filters import SearchFilter


# viewsets class combine both ListView class and DetailView class in one class

# level 1
# class ProfileList(generics.ListAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#     permission_classes = [IsAuthenticated]


# level 2
# class ProfileViewSet(ReadOnlyModelViewSet):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#     permission_classes = [IsAuthenticated]


# level 3
# can see the list of objects and update each of them also see a specific object detail
class ProfileViewSet(mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, IsOwnProfileOrReadOnly]

    # to filter the profiles with fields
    filter_backends = [SearchFilter]
    search_fields = ["city"]  # http://127.0.0.1:8000/api/profiles/?search=tehran
    # it also handles the partial search fields, for example if enter "teh" it also return
    # the result same as the above url test


# with ModelViewSet can create, read, update, and delete (CRUD) an instance of a model


class ProfileStatusViewSet(ModelViewSet):
    serializer_class = ProfileStatusSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        queryset = ProfileStatus.objects.all()
        username = self.request.query_params.get("username", None)
        if username is not None:
            queryset = queryset.filter(user_profile__user__username=username)
            # http://127.0.0.1:8000/api/status/?username=admin
        return queryset

    # to connect automatically the new profile status to the profile of the user making request
    # we have to override the perform_create method
    def perform_create(self, serializer):
        user_profile = self.request.user.profile
        serializer.save(user_profile=user_profile)


class AvatarUpdateView(generics.UpdateAPIView):
    serializer_class = ProfileAvatarSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        profile_object = self.request.user.profile
        return profile_object

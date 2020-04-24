from rest_framework import serializers
from profiles.models import Profile, ProfileStatus


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    avatar = serializers.ImageField(read_only=True)

    # we set here to read_only because, we will create a specific serializer
    # for avatar and a specific endpoint to upload avatar

    class Meta:
        model = Profile
        fields = "__all__"


class ProfileAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('avatar',)


class ProfileStatusSerializer(serializers.ModelSerializer):
    user_profile = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = ProfileStatus
        fields = "__all__"

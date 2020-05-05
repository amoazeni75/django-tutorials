from rest_framework import serializers
from questions.models import Answer, Question


class AnswerSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)  # to have string representation of author
    created_at = serializers.SerializerMethodField()  # this kind of fields is
    # for the cases we want to operate some staff before returning the value
    likes_count = serializers.SerializerMethodField()
    user_has_voted = serializers.SerializerMethodField()  # to understand the request.user has voted or not

    class Meta:
        model = Answer
        exclude = ["question", "voters", "updated_at"]

    def get_created_at(self, instance):
        # to customize the way that the time wants look like
        return isinstance.created_at.strftime("%B %d %Y")  # name of the month-day-year

    def get_likes_count(self, instance):
        return instance.voters.count()

    def get_user_has_voted(self, instance):
        request = self.context.get("request")
        return instance.voters.filter(pk=request.user.pk).exists()


class QuestionSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)  # to have string representation of author
    created_at = serializers.SerializerMethodField()  # this kind of fields is
    slug = serializers.SlugField(read_only=True)
    answers_count = serializers.SerializerMethodField()
    user_has_answered = serializers.SerializerMethodField()

    class Meta:
        model = Question
        exclude = ["updated_at"]

    def get_created_at(self, instance):
        # to customize the way that the time wants look like
        return instance.created_at.strftime("%B %d %Y")  # name of the month-day-year

    def get_answers_count(self, instance):
        return instance.answers.count()

    def get_user_has_answered(self, instance):
        request = self.context.get("request")
        return instance.answers.filter(author=request.user).exists()

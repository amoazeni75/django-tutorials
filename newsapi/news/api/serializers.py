from rest_framework import serializers
from news.models import Article

from django.utils.timesince import timesince
from datetime import datetime

"""
The following class represent creating a serializer class for a specific model class,
for example we write ArticleSerializerClass to serialize the Article Model which we implemented it.
Most of the functions and fields should be writen by us; actually, this is the simplest and basic way
"""

# class ArticleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     author = serializers.CharField()
#     title = serializers.CharField()
#     description = serializers.CharField()
#     body = serializers.CharField()
#     location = serializers.CharField()
#     publication_date = serializers.DateField()
#     active = serializers.BooleanField()
#     created_at = serializers.DateTimeField(read_only=True)
#     updated_at = serializers.DateTimeField(read_only=True)
#
#     def create(self, validated_data):
#         return Article.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.author = validated_data.get('author', instance.author)
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get('description', instance.description)
#         instance.body = validated_data.get('body', instance.body)
#         instance.location = validated_data.get('location', instance.location)
#         instance.publication_date = validated_data.get('publication_date', instance.publication_date)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
#
#     def validate(self, data):
#         """This function is a global validator for all of the parameters"""
#         if data["title"] == data["description"]:
#             raise serializers.ValidationError("Title and Description must be different from each other!")
#         return data
#
#     def validate_title(self, value):
#         """This function is a validator just for title field"""
#         if len(value) < 60:
#             raise serializers.ValidationError("The title must include at least 60 characters")
#         return value


"""
The ModelSerializerClass is the other way of serializing a model. This way includes less code
and some functions like create, update, etc. is ready to use. This way also provides automatic definition
of the fields

"""


class ArticleSerializer(serializers.ModelSerializer):
    # you can also define some fields added to the model's fields
    # 1: define the field you want to add to the fields
    # 2: define the get_name_of_ne_field() method
    time_since_publication = serializers.SerializerMethodField()

    class Meta:
        # 1: specify the model which wants to serialize
        model = Article

        # 2: specify the fields which wants to serialize
        # fields = "__all__"  # we want all the fields of our model
        # fields = ("title", "body", "description")  # we want to serialize just these fields
        exclude = ('id',)  # we want all the fields except these fields

    def get_time_since_publication(self, object):
        p_date = object.publication_date
        now = datetime.now()
        t_delta = timesince(p_date, now)
        return t_delta

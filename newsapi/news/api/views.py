from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from news.models import Article
from news.api.serializers import ArticleSerializer


@api_view(["GET", "POST"])
def article_list_create_api_view(request):
    """
    This function will return list of articles or create a new one by
    detecting the request.method type
    :param request:
    :return:
    """
    if request.method == "GET":
        articles = Article.objects.filter(active=True)
        serializer = ArticleSerializer(articles, many=True)
        # by setting many=True you tell drf that queryset contains mutiple items (a list of items) so drf needs to
        # serialize each item with serializer class (and serializer.data will be a list)
        # if you don't set this argument it means queryset is a single instance and serializer.
        # data will be a single object)
        return Response(serializer.data)  # serializer.data is json format
    elif request.method == "POST":
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

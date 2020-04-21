from django.urls import path
from news.api.views import (article_list_create_api_view, article_detail_api_view,
                            ArticleDetailAPIView, ArticleListCreateAPIView,
                            JournalistListCreateAPIView)

urlpatterns = [
    # 1: function based API
    # path("articles/", article_list_create_api_view, name='article-list'),
    # path("articles/<int:pk>/", article_detail_api_view, name='article-detail'),

    # 2: class based API, it self has two model for its serializer
    # 2-1: defining a class which inherit serializer class and implementing all things by ourselves
    # 2-2: using ModelsSerializer which is very simple and less code needed
    path("articles/",
         ArticleListCreateAPIView.as_view(),
         name='articles-list'),

    path("articles/<int:pk>/",
         ArticleDetailAPIView.as_view(),
         name='article-detail'),

    path("journalists/",
         JournalistListCreateAPIView.as_view(),
         name='journalist-list'),

]

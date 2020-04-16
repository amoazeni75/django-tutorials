from django.urls import path

from . import views

app_name = 'posts'  # this for using in the template

urlpatterns = [
    path("", views.PostList.as_view(), name="all"),
    path("new/", views.CreatePost.as_view(), name="create"),
    path("by/<int:username>/", views.UserPosts.as_view(), name="for_user"),
    path("by/<int:username>/<int:pk>/", views.PostDetail.as_view(), name="single"),
    path("delete/<int:pk>/", views.DeletePost.as_view(), name="delete"),
]

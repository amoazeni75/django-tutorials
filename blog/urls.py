from django.urls import path
from blog import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('about', views.AboutView.as_view(), name='about'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.CreatePostView.as_view(), name='post_new'),
    path('post/<int:pk>/edit', views.PostUpdateView.as_view(), 'post_edit'),
    path('post/<int:pk>/remove', views.PostDeleteView.as_view(), 'post_remove'),
    path('drafts', views.DraftListView.as_view(), 'post_draft_list'),
    path('post/<int:pk>/comment', views.add_comment_to_post, 'add_comment_to_post'),
    path('comment/<int:pk>/approve', views.comment_approve, 'comment_approve'),
]

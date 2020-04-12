from django.shortcuts import render
from django.views.generic import (TemplateView, ListView,
                                  DetailView, CreateView,
                                  UpdateView)
from blog.models import Post, Comment
from django.utils import timezone

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from blog.forms import PostFrom


# Create your views here.

class AboutView(TemplateView):
    template_name = 'about.html'


class PostListView(ListView):
    model = Post

    """
    This helps to use Django's ORM when dealing with such generic view, it is a version of
    writing SQL query in python
    """

    def get_queryset(self):
        """:param
        actually we get all the posts which their published date is less or equal to the now
        and sort them by the time near to now(the most recent post comes up front or at the top of the list)
        (using mines behind the field).
        when define the following function, instead of retuning whole objects, it will run your sql
        query to get the objects. for more information check out the db->query in the
        django documentation page
        """
        return Post.objects.filter(published_date__lte=timezone.now().order_by('-published_date'))


class PostDetailView(DetailView):
    model = Post


class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostFrom
    model = Post


class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostFrom
    model = Post

from django.shortcuts import render
from django.urls import reverse_lazy  # for the case when the user log in or log out where should go

from django.views.generic import CreateView

from accounts import forms


# Create your views here.

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

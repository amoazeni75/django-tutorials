from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from first_app.models import AccessRecord, WebPage, Topic
from . import form
from first_app.form import NewWebPageForm, UserForm, UserProfileInfoForm

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate


# Create your views here.

def index(request):
    # way 1: direct return
    # return HttpResponse("Hello world!")

    # way 2: return template
    my_dict = {'insert_me_variable': "Hello, I'am from views.py"}
    return render(request, 'first_app/index.html', context=my_dict)


def show_web_pages(request):
    web_pages = AccessRecord.objects.order_by('-date')
    date_dict = {'access_records': web_pages}
    return render(request, 'first_app/web_pages.html', context=date_dict)


def form_name_view(request):
    f_name = form.FormName()

    if request.method == 'POST':
        f_name = form.FormName(request.POST)
        # if f_name.is_valid():
        # # DO SOMETHING CODE
        # print("Name: " + f_name.cleaned_data['name'])
        # print("Email: " + f_name.cleaned_data['email'])
        # print("Text:" + f_name.cleaned_data['text'])

    return render(request, 'first_app/form.html', {'form': f_name})


@login_required
def register_web_page(request):
    f_new = NewWebPageForm()
    if request.method == 'POST':
        f_new = NewWebPageForm(request.POST)
        if f_new.is_valid():
            f_new.save(commit=True)
            return show_web_pages(request)
        else:
            print("register failed")
    return render(request, 'first_app/registerWebpage.html', {'form': f_new})


def register_user(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'first_app/registration.html',
                  {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('first_app:register_web_pages'))
            else:
                return HttpResponse("Account not active")
        else:
            print("log in failed")
            return HttpResponse("Invalid login")
    else:
        return render(request, 'first_app/login.html', {})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

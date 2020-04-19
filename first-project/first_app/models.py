from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



# Create your models here.
class Topic(models.Model):
    top_name = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.top_name


class WebPage(models.Model):
    topic = models.ForeignKey(Topic,
                              models.SET_NULL,
                              blank=True,
                              null=True, )
    name = models.CharField(max_length=256, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name


class AccessRecord(models.Model):
    name = models.ForeignKey(WebPage,
                             models.SET_NULL,
                             blank=True,
                             null=True, )
    date = models.DateField()

    def __str__(self):
        return str(self.date)


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE)  # bind each customized user to the default User of Django
    # Add other attributes to the user
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username


# for advance view, class based view
class School(models.Model):
    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    # this function tells the django that after creating a new instances of this page
    # what to do and where to go
    def get_absolute_url(self):
        return reverse('first_app:detail', kwargs={'pk': self.pk})


class Student(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School, models.SET_NULL,
                               blank=True,
                               null=True, related_name='students')

    def __str__(self):
        return self.name

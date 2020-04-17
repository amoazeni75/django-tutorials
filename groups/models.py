from django.db import models
from django.utils.text import slugify

# Create your models here.
import misaka

from django.contrib.auth import get_user_model

User = get_user_model()  # the user already logged in and active

from django import template

register = template.library


class Group(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, default='')
    description_html = models.TextField(blank=True, default='', editable=False)
    members = models.ManyToManyField(User, through='GroupMember')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reversed('groups:single', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['name']


class GroupMember(models.Model):
    group = models.ForeignKey(Group,
                              models.SET_NULL,
                              blank=True,
                              null=True,
                              related_name='memberships')
    user = models.ForeignKey(User,
                             models.SET_NULL,
                             blank=True,
                             null=True,
                             related_name='user_groups')  # the groups that the current user belongs to

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('group', 'user')

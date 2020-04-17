from django.contrib import admin
from blog.models import Post, Comment


# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    fields = ['author', 'created_date', 'approved_comment', 'text', 'post']


admin.site.register(Post)
admin.site.register(Comment, CommentAdmin)

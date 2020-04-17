from django.contrib import admin
from blog.models import Post, Comment


# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    fields = ['author', 'created_date', 'approved_comment', 'text', 'post']
    search_fields = ['author', 'text', 'post__title']  # add searching by tittle in the admin panel
    list_filter = ['post']
    list_display = ['id', 'author', 'created_date', 'post']
    list_display_links = None
    list_editable = ['post', 'author']


admin.site.register(Post)
admin.site.register(Comment, CommentAdmin)

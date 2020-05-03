from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUser


# Register your models here.


class CustomUserAdmin(UserAdmin):
    # when we added a new field in the CustomUser, we should update it here for the form
    # add_form =
    # form =
    model = CustomUser
    list_display = ["username", "email", "is_staff"]


admin.site.register(CustomUser, CustomUserAdmin)

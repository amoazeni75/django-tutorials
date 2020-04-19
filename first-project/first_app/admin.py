from django.contrib import admin
from first_app.models import WebPage, AccessRecord, Topic, UserProfileInfo, School, Student

# Register your models here.

admin.site.register(Topic)
admin.site.register(WebPage)
admin.site.register(AccessRecord)
admin.site.register(UserProfileInfo)
admin.site.register(School)
admin.site.register(Student)

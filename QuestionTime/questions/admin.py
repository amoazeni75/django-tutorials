from django.contrib import admin
from questions.models import Question, Answers

# Register your models here.


admin.site.register(Question)
admin.site.register(Answers)

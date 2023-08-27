from django.contrib import admin
from .models import college,branch,Student
# Register your models here.
admin.site.register(college)
admin.site.register(branch)
admin.site.register(Student)
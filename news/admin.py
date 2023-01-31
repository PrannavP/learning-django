from django.contrib import admin

# Register your models here.
from . models import Student, Teacher, Courses

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Courses)
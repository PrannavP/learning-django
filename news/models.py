from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    address = models.CharField(max_length=50)

class Teacher(models.Model):
    name = models.CharField(max_length=55)
    teaching_course = models.CharField(max_length=55, unique=True)

class Courses(models.Model):
    course_title = models.CharField(max_length=50, unique=True)
    course_price = models.CharField(max_length=10)
    course_length = models.CharField(max_length=20)
    course_description = models.CharField(max_length=100)
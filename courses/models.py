from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=100)
    teachers = models.CharField(max_length=200, default="")
    description = models.CharField(max_length=300, default="")
    category = models.CharField(choices=[
        ('Math', 'Math'),
        ('Science', 'Science'),
        ('Music', 'Music'),
        ('Computer Science', 'Computer Science'),
        ('Art', 'Art'),
    ], max_length=100, default="Math")
    grade = models.CharField(max_length=100)
    student_experience = models.CharField(max_length=300)
    student_workload = models.CharField(max_length=100)
    course_prereqs = models.CharField(max_length=200, default="")
    course_image = models.ImageField(upload_to="images/", default="images/defaultImage.jpeg")
    
from rest_framework import serializers #helps REST read data -> person
from .models import Course


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ['name', 'teachers', 'description', 'category', 'grade', 'student_experience', 'student_workload', 'course_prereqs', 'course_image']

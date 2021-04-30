# Create your views here.

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import CourseSerializer
from .models import Course

class CourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Course.objects.all() #all the courses 
    serializer_class = CourseSerializer

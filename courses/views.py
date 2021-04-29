# Create your views here.

#viewset:
#a set of operations that can be done on models

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import CourseSerializer
from .models import Course

class CourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    # def get_permissions(self):
    #     """
    #     Instantiates and returns the list of permissions that this view requires.
    #     """
    #     if self.action == 'list':
    #         permission_classes = []
    #     else:
    #         permission_classes = [permissions.IsAuthenticated]
    #     return [permission() for permission in permission_classes]


    #below tells django that we need to do GET/POST on all courses 
    #when GET/POST request happens, need to use CourseSerializer
    queryset = Course.objects.all() #all the courses 
    serializer_class = CourseSerializer

# Create your views here.

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ChatboxFormSerializer
from .models import ChatboxForm

class ChatboxFormViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ChatboxForm.objects.all() #all the forms 
    serializer_class = ChatboxFormSerializer

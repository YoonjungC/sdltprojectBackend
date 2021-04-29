from rest_framework import serializers #helps REST read data -> person
from .models import ChatboxForm


class ChatboxFormSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ChatboxForm
        fields = ['first_name', 'last_name', 'email', 'question']
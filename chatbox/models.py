from django.db import models

# Create your models here.

class ChatboxForm(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    question = models.CharField(max_length=100)
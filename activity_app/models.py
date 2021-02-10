from django.db import models
from django import forms
# Create your models here.
class Users(models.Model):
    email = models.EmailField(max_length=254)
    pwd = models.CharField(max_length=254)

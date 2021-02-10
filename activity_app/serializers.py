from rest_framework import serializers
from .models import Users


class Userserialzier(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['email','pwd']
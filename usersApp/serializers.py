from .models import UsersData
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersData
        fields = '__all__'
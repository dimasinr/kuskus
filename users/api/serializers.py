from rest_framework import serializers
from users.models import AbstractUser

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = AbstractUser
        fields = '__all__' 
        depth = 1
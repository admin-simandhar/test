from rest_framework import serializers
from User.models import User
class UserVSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["fullname","username","password"]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        depth = 1
        exclude=["password"]

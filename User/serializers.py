from rest_framework.serializers import ModelSerializer
from .models import UserModel

class UserLoginSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['email','password']
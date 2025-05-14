from rest_framework.serializers import ModelSerializer
from .models import TodoModel

class ListTodoSerializer(ModelSerializer):
    class Meta:
        model = TodoModel
        fields = "__all__"

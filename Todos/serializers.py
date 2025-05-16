from rest_framework.serializers import ModelSerializer
from .models import TodoModel

class ListTodoSerializer(ModelSerializer):
    class Meta:
        model = TodoModel
        fields = ["id",'work', 'deadline']

class RetrieveTodoSerializer(ModelSerializer):
    class Meta:
        model = TodoModel
        fields = ['id','work','deadline','created_at','is_finished']
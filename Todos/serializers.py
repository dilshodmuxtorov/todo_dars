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

class CreateTodoSerializer(ModelSerializer):
    class Meta:
        model = TodoModel
        fields = ["work",'deadline']
    
    def create(self, validated_data):
        user = self.context['request'].user  
        return TodoModel.objects.create(user_id=user, **validated_data)


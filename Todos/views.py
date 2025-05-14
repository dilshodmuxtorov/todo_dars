from rest_framework.generics import ListAPIView
from .models import TodoModel 
from .serializers import ListTodoSerializer
from User.authentication import CustomUserJWTAuthentication

class TodoListView(ListAPIView):
    authentication_classes = [CustomUserJWTAuthentication]
    serializer_class = ListTodoSerializer
    queryset = TodoModel.objects.all()
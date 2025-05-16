from rest_framework.generics import ListAPIView
from .models import TodoModel 
from .serializers import ListTodoSerializer, RetrieveTodoSerializer
from User.authentication import CustomUserJWTAuthentication
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class TodoListView(APIView):
    authentication_classes = [CustomUserJWTAuthentication]

    def get(self, request, *args, **kwargs):
        user_id = self.request.user
        user = TodoModel.objects.filter(user_id = user_id, is_finished = False)
        serializer = ListTodoSerializer(user, many = True)
        return Response(data=serializer.data, status= status.HTTP_200_OK)

class RetrieveTodoView(APIView):
    authentication_classes = [CustomUserJWTAuthentication]

    def get(self, request, pk):
        user_id = request.user
        try:
            todo = TodoModel.objects.get(pk = pk)
            if todo.user_id != user_id:
                return Response(data={"error":"Bu narsa sizga tegishli emas"}, status=status.HTTP_404_NOT_FOUND)
            else:
                serializer = RetrieveTodoSerializer(todo)
                return Response(data=serializer.data, status=status.HTTP_200_OK)
        except TodoModel.DoesNotExist:
            return Response(data={"error":"Ushbu idda malumot topilmadi"}, status=status.HTTP_404_NOT_FOUND)
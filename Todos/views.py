from rest_framework import generics
from .models import TodoModel 
from .serializers import ListTodoSerializer, RetrieveTodoSerializer, CreateTodoSerializer
from User.authentication import CustomUserJWTAuthentication
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


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
    
class CreateTodoView(generics.GenericAPIView):
    serializer_class = CreateTodoSerializer
    authentication_classes = [CustomUserJWTAuthentication]

    @swagger_auto_schema(
        request_body=CreateTodoSerializer,
        responses={201: 'Created', 400: 'Bad Request'}
    )
    def post(self, request):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"error": "Mistake on serializer", "details": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    

class DeleteTodoView(APIView):
    authentication_classes = [CustomUserJWTAuthentication]

    def delete(self , request, pk = None):
        try:
            todo = TodoModel.objects.get(pk = pk, user_id = request.user)
            todo.delete()
            return Response({"success":"deleted"}, status=status.HTTP_200_OK)
        except TodoModel.DoesNotExist:
            return Response({"error":"User topilmadi. YOki ro'yxatdan o'tilmagan"}, status=status.HTTP_404_NOT_FOUND)

class SetFinishedTrueView(APIView):
    authentication_classes = [CustomUserJWTAuthentication]

    def patch(self, request, pk = None):
        try:
            todo = TodoModel.objects.get(pk = pk, user_id = request.user)
            todo.is_finished = True
            todo.save()
            return Response({"success":"Set True"}, status=status.HTTP_200_OK)
        except TodoModel.DoesNotExist:
            return Response({"error":"User topilmadi. YOki ro'yxatdan o'tilmagan"}, status=status.HTTP_404_NOT_FOUND)
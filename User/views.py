from rest_framework.views import APIView
from rest_framework import generics
from .models import UserModel
from .serializers import UserLoginSerializer, UserGetSeralizer
from .authentication import CustomUserJWTAuthentication
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi



class LoginAPIView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            try:
                user = UserModel.objects.get(email=email, password=password)
                if user:
                    refresh_token = RefreshToken.for_user(user=user)
                    access_token = refresh_token.access_token
                    return Response({
                        "refresh_token": str(refresh_token),
                        "access_token": str(access_token)
                    }, status=status.HTTP_200_OK)
                else:
                    return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
            except UserModel.DoesNotExist:
                return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"errors": serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class UserInfoView(APIView):
    authentication_classes = [CustomUserJWTAuthentication]

    def get(self, request):
        user_id = self.request.user.id
        try:
            user = UserModel.objects.get(pk = user_id)
            serializer = UserGetSeralizer(self.request.user)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except UserModel.DoesNotExist:
            return Response({"error":"User Not Found"}, status=status.HTTP_404_NOT_FOUND)
        
class ImageUpdateView(APIView):
    authentication_classes = [CustomUserJWTAuthentication]
    @swagger_auto_schema(
        # operation_summary="Profil rasmini almashritish uchun api",
        operation_description="Profil rasmini alishtirish",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'image': openapi.Schema(type=openapi.TYPE_FILE, description="New user image"),
            }
        ),
        responses={200: "Image updated successfully", 400: "Invalid request"}
    )
    def put(self, request):
        user_id = self.request.user.id

        if 'image' not in self.request.FILES:
            return Response(data={"error":"Rasm hali yuklanmagan ukam!"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = UserModel.objects.get(id = user_id)
            new_image = self.request.FILES['image']
            if user.image:
                user.image.delete(save=True)

            user.image = new_image
            user.save()

            return Response(data={"success":"Rasm saqlandi bratishka"}, status=status.HTTP_200_OK)
        except UserModel.DoesNotExist:
            return Response(data={"error":"Topilmading ukam"}, status=status.HTTP_404_NOT_FOUND)




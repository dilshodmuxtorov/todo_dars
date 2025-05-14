from rest_framework.views import APIView
from rest_framework import generics
from .models import UserModel
from .serializers import UserLoginSerializer
from .authentication import CustomUserJWTAuthentication
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

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
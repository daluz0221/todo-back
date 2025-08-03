from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from .serializers import CustomTokenRefreshSerializer



from shared.adapters import return_refresh_token

from .serializers import UserRegisterSerializer, UserLoginSerializer


class RegisterApiView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

       
            dict_response = return_refresh_token(user)
            dict_response.update({
                'message': 'Usuario registrado correctamente'
            })
            return Response(dict_response,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class LoginApiview(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutApiView(APIView):

    def post(self, request):
        refresh_token = request.data.get("refresh")
        print("#hola")

        if not refresh_token:
            return Response({
                "Detail": "No se proporcionó el token de refresco"
            }, status=status.HTTP_400_BAD_REQUEST)
    
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({
                "Detail": "Sesión cerrada correctamente"
            }, status=status.HTTP_205_RESET_CONTENT)
        except TokenError as e:
            return Response({"detail": str(e)},
                            status=status.HTTP_400_BAD_REQUEST)
        

class CustomTokenRefreshView(TokenRefreshView):
    permission_classes = [AllowAny]
    

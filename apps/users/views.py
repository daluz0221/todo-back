from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny



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
    
    
    
# TODO: crear un middleware para todas las peticiones a las APIs que no sean de registro o login
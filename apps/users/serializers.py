from rest_framework.serializers import ModelSerializer, Serializer, CharField, EmailField
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import get_user_model, authenticate

from shared.adapters import return_refresh_token

User = get_user_model()

class UserRegisterSerializer(ModelSerializer):

    password = CharField(write_only=True, min_length=10)

    class Meta:
        model = User
        fields =[
            'email',
            'username',
            'first_name',
            'last_name',
            'password'
        ]
        extra_kwargs = {
            'first_name': {'required': False, 'allow_blank': True},
            'last_name': {'required': False, 'allow_blank': True},
        }

    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    


class UserLoginSerializer(Serializer):
    email = EmailField()
    password = CharField(write_only=True)

    def validate(self, data):
        user = authenticate(email=data['email'], password=data['password'])
   
        if not user:
            raise ValidationError("Credenciales inválidas.")
        if not user.is_active:
            raise ValidationError("La cuenta está desactivada.")
   

        return return_refresh_token(user)
    

class CustomTokenRefreshSerializer(TokenRefreshSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        # El token de refresco viene en attrs['refresh']
        refresh_token = attrs['refresh']

        # Crear instancia de RefreshToken para poder rotarlo

        refresh = RefreshToken(refresh_token)

        # Si tienes ROTATE_REFRESH_TOKENS=True, al llamar a refresh.blacklist()
        # y luego generar uno nuevo, aquí puedes obtener el nuevo refresh token
        # (este paso depende de tu configuración)

        # Por defecto, cuando se llama super().validate(attrs), se crea un nuevo access token,
        # pero no se devuelve nuevo refresh token.

        # Para devolver también el refresh token, se debe hacer lo siguiente:

       
            # Esto depende de la versión y configuración, pero por seguridad puedes devolver el refresh token original
        data['refresh'] = str(refresh)

        return data
        
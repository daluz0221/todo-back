from rest_framework.serializers import ModelSerializer, Serializer, CharField, EmailField
from rest_framework.exceptions import ValidationError

from django.contrib.auth import get_user_model, authenticate

from shared.adapters import return_refresh_token

User = get_user_model()

class UserRegisterSerializer(ModelSerializer):

    password = CharField(write_only=True, min_length=10)

    class Meta:
        model = User
        fields =[
            'id',
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
        print(f"AUTENTICATE RETURNED: {user}")
        if not user:
            raise ValidationError("Credenciales inválidas.")
        if not user.is_active:
            raise ValidationError("La cuenta está desactivada.")
   

        return return_refresh_token(user)
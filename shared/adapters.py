from rest_framework_simplejwt.tokens import RefreshToken






def return_refresh_token(user):

    refresh = RefreshToken.for_user( user )

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        'user': {
            'id': user.id,
            'email': user.email,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
        }
    }
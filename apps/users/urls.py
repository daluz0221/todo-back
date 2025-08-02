from django.urls import path
from .views import RegisterApiView, LoginApiview, LogoutApiView, CustomTokenRefreshView

app_name = 'users_app'

urlpatterns = [
    path('register/', RegisterApiView.as_view(), name='register'),
    path('login/', LoginApiview.as_view(), name='login'),
    path('logout/', LogoutApiView.as_view(), name='logout'),
    path('refresh/', CustomTokenRefreshView.as_view(), name='refresh_token')
]
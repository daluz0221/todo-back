from django.urls import path
from .views import RegisterApiView, LoginApiview

app_name = 'users_app'

urlpatterns = [
    path('register/', RegisterApiView.as_view(), name='register'),
    path('login/', LoginApiview.as_view(), name='login'),
]
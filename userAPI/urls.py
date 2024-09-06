from django.urls import path, include

from .views import TestView, UserView, UserLoginView, UserVerificationView
from rest_framework_simplejwt import views as jwt_views
urlpatterns = [
    path('test', TestView.as_view()),
    path('create-user/', UserView.as_view()),
    path('get-user', UserLoginView.as_view()),
    path('login-user/', UserLoginView.as_view()),
    path('verify-user/<str:pk>', UserVerificationView.as_view()),
]
 
# Main Url /api/v1.0/user
# /api/v1.0/user/test
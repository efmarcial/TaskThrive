from django.urls import path, include

from .views import TestView, UserView

urlpatterns = [
    path('test/', TestView.as_view()),
    path('create-user/', UserView.as_view()),
]

# Main Url /api/v1.0/user
# /api/v1.0/user/test
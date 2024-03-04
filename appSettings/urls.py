from django.urls import path, include
from .views import SettingsView

urlpatterns = [
    path('settings', SettingsView.as_view()),
    path('create-new-setting/', SettingsView.as_view())
    
]

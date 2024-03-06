from django.urls import path, include
from .views import SettingsView

urlpatterns = [
    path('settings', SettingsView.as_view()), # URL to GET Settigns
    path('create-new-setting/', SettingsView.as_view()) # URL to POST new setting
    
]

# /api/v1.0/app/settings
# /api/v1.0/app/create-new-setting
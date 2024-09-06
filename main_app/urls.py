from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = [
    path('services_list/', views.service_list),
    path('services/<int:pk>/', views.service_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
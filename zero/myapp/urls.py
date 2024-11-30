# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.empty_view, name='empty'),
    path('data/', views.data_view, name='data'),
    path('test/', views.test_view, name='test'),
]
from django.urls import path
from . import views


app_name = 'generator'

urlpatterns = [
    path('', views.home, name='generator'),
    path('password/', views.password, name='password'),
    path('information/', views.information, name='info'),
]
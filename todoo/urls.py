from django.urls import path
from . import views


app_name = 'todoo'

urlpatterns = [
    path('singup/', views.singupUser, name='singup_todoo'),
    path('logout/', views.logoutUser, name='logoutUser'),
    path('login/', views.loginUser, name='loginUser'),

    
    path('create/', views.createtodoo, name='createtodoo'),
    path('current/', views.currenttodoo, name='currenttodoo'),
    path('complited/', views.complitedtodoo, name='complitedtodoo'),
    path('<int:todoo_pk>/', views.viewtodoo, name='viewtodoo'),
    path('<int:todoo_pk>/complite', views.complitetodoo, name='complitetodoo'),
    path('<int:todoo_pk>/delete', views.deletetodoo, name='deletetodoo'),
]
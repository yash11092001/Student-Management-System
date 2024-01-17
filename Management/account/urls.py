from django.urls import path
from account.views import *
urlpatterns=[
    path('login/',login,name='login'),
    path('register/',register,name='register'),
    path('dashboard/',dashboard,name='dashboard'),
    path('logout/',logout,name='logout'),
    path('details/<id>/',student_details,name='details'),
    path('delete/<id>/',delete,name='delete'),


]
from django.urls import path
from Student.views import *
urlpatterns = [
   path('',home,name='home'),
   path('record/',record,name='record'),
   path('registration/',registration,name='registration'),
   path('about/',about_us,name='about'),
   path('python/',python,name='python'),
   path('java/',java,name='java'),
   path('aws/',aws,name='aws'),


]
from django.urls import path		 
from . import views

urlpatterns=[ 
    path ('',views.generator),
    path ('/reset',views.reset),  
]
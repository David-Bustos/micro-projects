from django.urls import path		 
from . import views

urlpatterns=[ 
    path ('',views.menu),
    path ('/process_money',views.money, name='p_money'), 
    path ('/restart',views.restart, name='restart'), 
]

from django.urls import path
from app import views

urlpatterns=[
    path('index/', views.index),
    path('addUser', views.addUser),
    path('seeUser', views.seeUser),
    path('request', views.ggxx),
    path('userlist', views.userlist),
    path('alllist', views.alllist),
    path('gplist', views.gplist),
    path('gpdel', views.gpdel),
    path('lookGp', views.lookGp)
]
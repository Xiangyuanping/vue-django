
from django.urls import path
from app import views

urlpatterns=[
    path('index/', views.index),
    path('addUser/', views.addUser),
    path('api/seeUser/', views.seeUser),
    path('gpxx', views.request),
    path('userlist', views.userlist),
    path('alllist', views.alllist),
    path('gplist', views.gplist),
    path('lookGp', views.lookGp),
    path('request', views.ckmx)
]
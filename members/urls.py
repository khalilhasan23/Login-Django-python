from django.urls import path  
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('', views.login, name='login'),
    path('wrong/', views.wrong, name='wrong'),
]
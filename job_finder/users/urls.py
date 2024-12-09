from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register_user'),
    path('profile/', views.manageprofile, name='manage_profile'),
  
]

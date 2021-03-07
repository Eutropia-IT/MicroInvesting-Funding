from django.urls import path, include
from . import views

urlpatterns = [
    path('profile/',views.showProfilePage),
    path('profile/edit/',views.showEditProfilePage),
]

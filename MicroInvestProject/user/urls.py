from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.showProfilePage),
    path('edit/',views.showEditProfilePage),
    path('history/',views.showHistoryPage),
]

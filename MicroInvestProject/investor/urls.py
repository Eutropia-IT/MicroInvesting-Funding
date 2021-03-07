from django.urls import path, include
from . import views

urlpatterns = [
    path('dashboard/',views.showDashboardPage),
    path('profile/',views.showProfilePage),
    path('explore/',views.showExplorePage),
]

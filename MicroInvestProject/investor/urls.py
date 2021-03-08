from django.urls import path, include
from . import views

urlpatterns = [
    path('dashboard/',views.showDashboardPage),
    path('explore/',views.showExplorePage),
]

from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:proj__id>/', views.showSingleProject),
    
]
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def showProfilePage(request):
    return render(request, 'user/profile.html')
def showEditProfilePage(request):
    return render(request, 'user/edit_profile.html')

from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def showProfilePage(request):
    return render(request, 'profile/profile.html')
def showEditProfilePage(request):
    return render(request, 'profile/edit_profile.html')
def showHistoryPage(request):
    return render(request, 'profile/history.html')
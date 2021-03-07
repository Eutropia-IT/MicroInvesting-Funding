from django.http.response import HttpResponse
from django.shortcuts import render

def showLandingPage(request):
    return render(request, 'login/home.html')
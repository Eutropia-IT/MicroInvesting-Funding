from django.http.response import HttpResponse
from django.shortcuts import render

def showLandingPage(request):
    myDictonary = {
        "name" : "Al Amin",
        "age" : 12
    }
    return render(request, 'landing/index.html')

def signUpPage(request):
    return render(request, 'landing/signup.html')
from django.http.response import HttpResponse
from django.shortcuts import render

def showLandingPage(request):
    myDictonary = {
        "name" : "Al Amin",
        "age" : 12
    }
    return render(request, 'login/home.html', myDictonary)
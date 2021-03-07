from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def showProfilePage(request):
    return HttpResponse("This is profile page")

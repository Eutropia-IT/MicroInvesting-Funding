from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def showDashboardPage(request):
    return HttpResponse("This is dashboard page")
def showProfilePage(request):
    return HttpResponse("This is profile page")
def showExplorePage(request):
    return HttpResponse("This is explore page")
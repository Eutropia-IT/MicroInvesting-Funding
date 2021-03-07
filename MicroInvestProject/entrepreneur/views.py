from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def showDashboardPage(request):
    return HttpResponse("This is dashboard page")
def showApplyPage(request):
    return HttpResponse("This is apply now page")
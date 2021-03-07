from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def showDashboardPage(request):
    return HttpResponse("This is dashboard page")
def showReviewFormPage(request):
    return HttpResponse("This is application review page.\nhere analyst will call entrepreneur for interview or submit reviews about the proposed project and approve or reject the project after interview.")
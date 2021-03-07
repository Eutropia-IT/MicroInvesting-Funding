from django.http.response import HttpResponse
from django.shortcuts import render

def showDashboardPage(request):
    return render(request, 'investor/dashboard.html')
def showExplorePage(request):
    return render(request, 'investor/explore.html')
from django.http.response import HttpResponse
from django.shortcuts import render

def showDashboardPage(request):
    return render(request, 'entrepreneur/dashboard.html')
def showApplyPage(request):
    return render(request, 'entrepreneur/apply.html')
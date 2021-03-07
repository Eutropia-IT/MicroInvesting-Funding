from django.http.response import HttpResponse
from django.shortcuts import render

def showDashboardPage(request):
    return render(request, 'analyst/dashboard.html')
    
def showReviewFormPage(request):
    return render(request, 'analyst/review.html')
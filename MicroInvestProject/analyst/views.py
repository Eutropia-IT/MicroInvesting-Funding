from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from user.models import User
from entrepreneur.models import Projects

def showDashboardPage(request):
    try:
        if 'login' in request.session:
            content = { 'userData' :User.objects.get(id = request.session.get('userID')) }
            content['projLIst'] = Projects.objects.all()
            
            return render(request, 'analyst/index.html', content)
        else:
            messages.error(request, 'Please Login at First')
            return redirect('/') #return to home page cz of without login
    except KeyError:
        pass
    #return render(request, 'analyst/dashboard.html')
    
def showReviewFormPage(request):
    return render(request, 'analyst/review.html')
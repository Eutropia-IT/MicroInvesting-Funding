from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from user.models import User

def showDashboardPage(request):
    try:
        if 'login' in request.session:
            userData = { 'uData' : User.objects.get(id = request.session.get('userID')) }
            return render(request, 'investor/index.html', userData)
        else:
            messages.error(request, 'Please Login at First')
            return redirect('/') #return to home page cz of without login
    except KeyError:
        pass
def showExplorePage(request):
    return render(request, 'investor/explore.html')

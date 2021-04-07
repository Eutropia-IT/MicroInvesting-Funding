from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages

def showDashboardPage(request):
    try:
        if 'login' in request.session:
            #userData = { 'uData' : User.objects.get(id = request.session.get('userID')) }
            return render(request, 'entrepreneur/index.html')
        else:
            messages.error(request, 'Please Login at First')
            return redirect('/') #return to home page cz of without login
    except KeyError:
        pass
def showApplyPage(request):
    try:
        if 'login' in request.session:
            #userData = { 'uData' : User.objects.get(id = request.session.get('userID')) }
            return render(request, 'entrepreneur/apply.html')
        else:
            messages.error(request, 'Please Login at First')
            return redirect('/') #return to home page cz of without login
    except KeyError:
        pass
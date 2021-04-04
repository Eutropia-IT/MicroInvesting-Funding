from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from user.models import User

def showDashboardPage(request):
    try:
        if 'login' in request.session:
            userData = User.objects.filter(id = request.session.get('userData'))
            return render(request, 'investor/index.html', {'uData' : userData[0]})
        else:
            messages.error(request, 'Please Login at First')
            return redirect('/') #return to home page cz of without login
    except KeyError:
        pass
def showExplorePage(request):
    return render(request, 'investor/explore.html')

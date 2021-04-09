from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from user.models import User
from entrepreneur.models import Projects

# Create your views here.

def showSingleProject(request, proj__id):
    try:
        if 'login' in request.session:
            content = { 'selectedProject' : Projects.objects.get(id = proj__id)}
            #content = { 'uData' : User.objects.get(id = request.session.get('userID')) }
            
            print(User.objects.get(id= request.session.get('userID')))
            

            return render(request, 'projects/index.html', content)
        else:
            messages.error(request, 'Please Login at First')
            return redirect('/') #return to home page cz of without login
    except KeyError:
        pass
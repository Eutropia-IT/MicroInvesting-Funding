from django.http.response import HttpResponse
from django.shortcuts import render
from user.models import User


def showLandingPage(request):
    return render(request, 'landing/index.html')

def signUpPage(request):
    if request.method == 'POST':
        if request.POST.get('name') \
            and request.POST.get('cell') \
            and request.POST.get('nid') \
            and request.POST.get('dob') \
            and request.POST.get('email') \
            and request.POST.get('password'):
            
            var = User()
            var.name = request.POST.get('name')
            var.nid = request.POST.get('nid')
            var.dob = request.POST.get('dob')
            var.cell = request.POST.get('cell')
            var.email = request.POST.get('email')
            var.password = request.POST.get('password')
            var.save()
            return render(request, 'landing/index.html')
    else:
        return render(request, 'landing/signup.html')
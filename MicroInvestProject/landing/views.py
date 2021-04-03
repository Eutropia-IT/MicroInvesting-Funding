from django.shortcuts import render,redirect
from django.contrib import messages

from user.models import User
from django.db import IntegrityError
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist


def showLandingPage(request):
    if request.method == 'POST':
        useremail= request.POST.get('email')  
        userpassword = request.POST.get('password')
        
        try:
            qs1 = User.objects.get(email=useremail)
            try:
                qs2 = User.objects.get(password=userpassword)
                return redirect('investor/dashboard/')
            except ObjectDoesNotExist as e:
                if 'User matching query does not exist' in e.args[0]:
                    messages.error(request, 'Wrong Email or Password', )
                    return redirect('/')
            except MultipleObjectsReturned:
                return redirect('investor/dashboard/')
                
        except ObjectDoesNotExist as e:
            if 'User matching query does not exist' in e.args[0]:
                messages.error(request, 'Wrong Email or Password', )
                return redirect('/')
    
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
            try:
                var.save()
                messages.success(request, 'We just need to verify your email address before you can access. Verify your email address')
                return redirect('/signup')
            except IntegrityError as e:
                if 'UNIQUE constraint failed' in e.args[0]:
                    messages.error(request, 'It seems that this NID or Email is already associated with another account', )
                    return redirect('/signup')

            
            
    else:
        return render(request, 'landing/signup.html')
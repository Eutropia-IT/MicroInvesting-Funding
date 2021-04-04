from django.shortcuts import render,redirect
from django.contrib import messages
from user.models import User
from django.db import IntegrityError
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist


def showLandingPage(request):
    if 'login' in request.session:
        return redirect('investor/dashboard/')
    elif request.method == 'POST':
        useremail= request.POST.get('email')  
        userpassword = request.POST.get('password')
        if useremail and userpassword:
            getUser = User.objects.filter(email=useremail, password = userpassword)
            if getUser:
                request.session['login'] = True
                request.session['userData'] = getUser[0].id
                return redirect('investor/dashboard/')
            else:
                messages.error(request, 'Wrong Email or Password')
                return redirect('/')
    else:    
        print(request.session.get('userData'))
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

def logout(request):
    try:
        del request.session['login']
        del request.session['userData']
    except KeyError:
        pass
    return redirect('/')
import hashlib
import string
import random
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from user.models import User
from django.db import IntegrityError
from landing.models import ResetPssDB
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist

from django.conf import settings
from django.core.mail import EmailMultiAlternatives


def showLandingPage(request):
    if 'login' in request.session:
        userData = User.objects.get(id = request.session.get('userID'))
        if userData.isAnalyst == True:
            return redirect('analyst/dashboard/') # for analyst user
        else:
            return redirect('investor/dashboard/') #for general user
    elif request.method == 'POST':
        useremail= request.POST.get('email')  
        userpassword = request.POST.get('password')

        if useremail and userpassword:
            getUser = User.objects.filter(email=useremail, password = userpassword)
            if getUser:
                request.session['login'] = True
                request.session['userID'] = getUser[0].id
                if getUser[0].isAnalyst == True:
                    return redirect('analyst/dashboard/') # after successfull login go to analyst user
                else:
                    return redirect('investor/dashboard/') # after successfull login go to general user
            else:
                messages.error(request, 'Wrong Email or Password')
                return redirect('/')
    else:    
        #print(request.scheme)
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
        del request.session['userID']
    except KeyError:
        pass
    return redirect('/')

def forgotPassword(request):
    ramdom_str = ''.join(random.choice(string.ascii_lowercase) for i in range(40)) 
    current_site_link = get_current_site(request)
    if request.method == 'POST':
        getEmail = User.objects.filter(email=request.POST.get('email'))
        if(getEmail):
            x = ResetPssDB()
            x.applyUserEmail = getEmail[0].email
            x.secritKey = ramdom_str
            x.save()
            #textMessage = 'Your Recovary LinkL'+" "+"http://"+current_site_link.domain+"/"+ramdom_str
            asd = '<a href="' + request.scheme + '://'+ current_site_link.domain + '/reset-password/'+ ramdom_str + '"> Recovary Link </a>'
            subject, from_email, to = 'Password Recovary', '18201008@uap-bd.edu', getEmail[0].email
            text_content = 'Your Recovary Link'
            html_content = asd
            
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            messages.success(request, 'A recovery mail send to your email addresss. Please chack your email address.')
            return redirect('/')
        else:
            messages.error(request, 'Invalied Email!')
            return redirect('/')
    return render(request, 'landing/forgotPassword.html')

def resetPassword(request, skey):
    varifyKEY = ResetPssDB.objects.filter(secritKey=skey)
    if(varifyKEY):
        if request.method =='POST':
            var =  User.objects.get(email=varifyKEY[0].applyUserEmail)
            var.password = request.POST.get('password')
            var.save()
            messages.success(request, 'Password Changed Successfully.')
            return redirect('/')
        return render(request, 'landing/resetPassword.html')
    else:
        messages.error(request, 'Invalied Operaton')
        return redirect('/')



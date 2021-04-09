from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from user.models import User,Transaction

# Create your views here.

def addBalance(request):
    try:
        if 'login' in request.session:
            
            if request.method == 'POST':
                if request.POST.get('amount'):
                    #userData.totalInvested = userData.totalInvested + float(request.POST.get('amount'))
                    #userData.save()
                    #Transaction().user_ID_id = User()
                    Transaction().amount = 500.00
                    Transaction().trans_type = 'deposit'
                    Transaction().save()
                    messages.success(request, 'Successfully Transection.')
                    return redirect('/investor/dashboard')
            return render(request, 'transection/addBalance.html')
        else:
            messages.error(request, 'Please Login at First')
            return redirect('/') #return to home page cz of without login
    except KeyError:
        pass


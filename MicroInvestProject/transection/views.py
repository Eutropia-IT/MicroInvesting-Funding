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
                    transectionTable = Transaction()
                    transectionTable.trans_type = 'deposit'
                    transectionTable.user_ID = User.objects.get(id= request.session.get('userID'))
                    transectionTable.amount = request.POST.get('amount')
                    transectionTable.save()
                    messages.success(request, 'Successfully Transection.')
                    return redirect('/investor/dashboard')
            return render(request, 'transection/addBalance.html')
        else:
            messages.error(request, 'Please Login at First')
            return redirect('/') #return to home page cz of without login
    except KeyError:
        pass


from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from user.models import User,Transaction
from re import search
# Create your views here.

def addBalance(request):
    try:
        if 'login' in request.session:
            userTable = User.objects.get(id=request.session.get('userID'))
            var = request.META.get('HTTP_REFERER')
            content = { 'prevURL': var}
            if request.method == 'POST':
                if request.POST.get('amount'):
                    transectionTable = Transaction()
                    transectionTable.trans_type = 'deposit'
                    transectionTable.user_ID = User.objects.get(id= request.session.get('userID'))
                    transectionTable.amount = request.POST.get('amount')
                    userTable.currentBalance += float(request.POST.get('amount'))
                    transectionTable.save()
                    userTable.save() 
                    messages.success(request, 'Successfully Transection.')
                    if search('investor', request.POST.get('prevURL')):
                        return redirect('/investor/dashboard')
                    elif search('entrepreneur', request.POST.get('prevURL')):
                        return redirect('/entrepreneur/dashboard')
            return render(request, 'transection/addBalance.html', content )
        else:
            messages.error(request, 'Please Login at First')
            return redirect('/') #return to home page cz of without login
    except KeyError:
        pass

def withdrawBalance(request):
    try:
        if 'login' in request.session:
            userTable = User.objects.get(id=request.session.get('userID'))
            var = request.META.get('HTTP_REFERER')
            content = { 'prevURL': var}
            if request.method == 'POST':
                if request.POST.get('amount'):
                    transectionTable = Transaction()
                    transectionTable.trans_type = 'withdraw'
                    transectionTable.user_ID = User.objects.get(id= request.session.get('userID'))
                    transectionTable.amount = request.POST.get('amount')
                    userTable.currentBalance -= float(request.POST.get('amount'))
                    transectionTable.save()
                    userTable.save() 
                    messages.success(request, 'Successfully Transection.')
                    if search('investor', request.POST.get('prevURL')):
                        return redirect('/investor/dashboard')
                    elif search('entrepreneur', request.POST.get('prevURL')):
                        return redirect('/entrepreneur/dashboard')
            return render(request, 'transection/withdrawBalance.html',content)
        else:
            messages.error(request, 'Please Login at First')
            return redirect('/') #return to home page cz of without login
    except KeyError:
        pass

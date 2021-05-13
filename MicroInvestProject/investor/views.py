from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from user.models import User, Transaction
from entrepreneur.models import Projects
from django.db.models import Sum
from investor.models import Investment
from django.core.files.storage import FileSystemStorage

def showDashboardPage(request):
    try:
        if 'login' in request.session:
            content = { 'uData' : User.objects.get(id = request.session.get('userID')) }
            content['projList'] = Projects.objects.all()
            content['profit'] = content['uData'].totalRepaid - content['uData'].totalInvested 
            content['totalMembers'] = User.objects.all().count()
            content['totalInvestor'] = User.objects.filter(isInvestor=True).count()
            content['totalInvested'] = User.objects.aggregate(Sum('totalInvested'))
            content['totalRepaid'] = User.objects.aggregate(Sum('totalRepaid'))
           
            if request.method == 'POST':
                if len(request.FILES) != 0:
                    content['uData'].profileImage = request.FILES['profileImage']
                    content['uData'].save()
                    messages.success(request, 'Profile Picture Changed Successfully.')
                    return redirect('/investor/dashboard')
                if  request.POST.get('cPassword') and request.POST.get('password')==content['uData'].password:
                    content['uData'].password = request.POST.get('cPassword')
                    content['uData'].save()
                    messages.success(request, 'Passwoed Changed Successfully.')
                    return redirect('/investor/dashboard') 
                elif request.POST.get('email')==content['uData'].email and request.POST.get('cell') and request.POST.get('password')==content['uData'].password:
                    content['uData'].email = request.POST.get('email')
                    content['uData'].cell = request.POST.get('cell')
                    content['uData'].password = request.POST.get('password')
                    content['uData'].save()
                    messages.success(request, 'Profile Updated Successfully.')
                    return redirect('/investor/dashboard')
                elif request.POST.get('email')!=content['uData'].email and request.POST.get('cell') and request.POST.get('password')==content['uData'].password and User.objects.filter(email=request.POST.get('email')).count()<=0:
                    content['uData'].email = request.POST.get('email')
                    content['uData'].cell = request.POST.get('cell')
                    content['uData'].password = request.POST.get('password')
                    content['uData'].save()
                    messages.success(request, 'Profile Updated Successfully.')
                    return redirect('/investor/dashboard')
                else:
                    messages.error(request, 'Invalied Email or Password!')
                    return redirect('/investor/dashboard') 
                
            else:
                print(content['uData'].profileImage)
                return render(request, 'investor/index.html', content)
        else:
            messages.error(request, 'Please Login at First')
            return redirect('/') #return to home page cz of without login
    except KeyError:
        pass
def showExplorePage(request):
    return render(request, 'investor/explore.html')


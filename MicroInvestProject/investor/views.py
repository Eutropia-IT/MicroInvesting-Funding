from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from user.models import User
from entrepreneur.models import Projects

def showDashboardPage(request):
    try:
        if 'login' in request.session:
            content = { 'uData' : User.objects.get(id = request.session.get('userID')) }
            content['projList'] = Projects.objects.all()
            
            if request.method == 'POST':
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
                return render(request, 'investor/index.html', content)
        else:
            messages.error(request, 'Please Login at First')
            return redirect('/') #return to home page cz of without login
    except KeyError:
        pass
def showExplorePage(request):
    return render(request, 'investor/explore.html')


from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from user.models import User
from entrepreneur.models import Projects
from investor.models import Investment

# Create your views here.

def showSingleProject(request, proj__id):
    try:
        if 'login' in request.session:
            content = { 'selectedProject' : Projects.objects.get(id = proj__id)}
            content['uData'] = User.objects.get(id = request.session.get('userID'))
            #content['selectedProject'].feedback1
            if request.method == 'POST':
                if request.POST.get('rating') and request.POST.get('feedBack'):
                    if content['uData'].id == 1:
                        content['selectedProject'].profit_Indicator1 = request.POST.get('rating')
                        content['selectedProject'].feedback1 = request.POST.get('feedBack')
                        content['selectedProject'].proj_status = 'active'
                        content['selectedProject'].save() 
                        messages.success(request, 'Succcessgully Reating This Project.')
                        return redirect('/analyst/dashboard')
                    elif content['uData'].id == 2:
                        content['selectedProject'].profit_Indicator2 = request.POST.get('rating')
                        content['selectedProject'].feedback2 = request.POST.get('feedBack')
                        content['selectedProject'].proj_status = 'active'
                        content['selectedProject'].save() 
                        messages.success(request, 'Succcessgully Reating This Project.')
                        return redirect('/analyst/dashboard')
                    elif content['uData'].id == 3:
                        content['selectedProject'].profit_Indicator3 = request.POST.get('rating')
                        content['selectedProject'].feedback3 = request.POST.get('feedBack')
                        content['selectedProject'].proj_status = 'active'
                        content['selectedProject'].save() 
                        messages.success(request, 'Succcessgully Reating This Project.')
                        return redirect('/analyst/dashboard')
                    else:
                        messages.error(request, 'You are not authorize Analyst!')
                        return redirect('/analyst/dashboard')
                else:
                    investTable = Investment()
                    investTable.investor_ID = User.objects.get(id= request.session.get('userID'))
                    investTable.proj_ID = Projects.objects.get(id= proj__id)
                    investTable.amount = request.POST.get('amount')
                    investTable.save()
                    messages.success(request, 'Succcessgully Invested.')
                    return redirect('/')
            else:
                return render(request, 'projects/index.html', content)
        else:
            messages.error(request, 'Please Login at First')
            return redirect('/') #return to home page cz of without login
    except KeyError:
        pass
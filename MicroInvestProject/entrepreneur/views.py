from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from entrepreneur.models import Projects
from user.models import User


def showDashboardPage(request):
    try:
        if 'login' in request.session:
            content = { 'uData' : User.objects.get(id = request.session.get('userID')) }
            content['uProjectList'] = Projects.objects.filter( entr_ID= request.session.get('userID'))
            print(content['uProjectList'][0].proj_status)
            return render(request, 'entrepreneur/index.html', content)
        else:
            messages.error(request, 'Please Login at First')
            return redirect('/') #return to home page cz of without login
    except KeyError:
        pass
def showApplyPage(request):
    try:
        if 'login' in request.session:
            #userData = { 'uData' : User.objects.get(id = request.session.get('userID')) }
            if request.method == 'POST':
                loadProjectTable = Projects()
                loadProjectTable.entr_ID = User.objects.get(id = request.session.get('userID'))
                loadProjectTable.proj_Name = request.POST.get('projrctName')
                loadProjectTable.proj_Location = request.POST.get('ProjectArea')
                loadProjectTable.proj_Budget = float(request.POST.get('potentialBudget'))
                loadProjectTable.proj_details = request.POST.get('despcription')
                loadProjectTable.save()
                messages.success(request, 'Successfully aplied your idea.')
                return redirect('/entrepreneur/dashboard')
            else:
                return render(request, 'entrepreneur/apply.html')
        else:
            messages.error(request, 'Please Login at First')
            return redirect('/') #return to home page cz of without login
    except KeyError:
        pass
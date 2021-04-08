from django.shortcuts import render

# Create your views here.

def showSingleProject(request, proj__id):
    return render(request, 'projects/index.html')
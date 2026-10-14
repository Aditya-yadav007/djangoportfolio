from django.shortcuts import render
from .models import Project

def Aditya(request):
    projects = Project.objects.all()
    return render(request, "main.html", {"projects": projects})

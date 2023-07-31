from django.shortcuts import render
from .models import Student

def index(request):
    return render(request,"index.html")
def getname(request):
    regno=request.GET['regno']
    name=Student.objects.get(regno=regno)
    context = {
        'name':name
    }
    return render(request, "getname.html",context)
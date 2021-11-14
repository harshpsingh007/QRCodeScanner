from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Scanned
import time

# Create your views here.
def Home(request):
    scan = Scanned.objects.all()
    for i in scan:
        num = i.num
    return render(request,"home.html",{'num':num})

def Add(request):
    return render(request,"add.html")

def Subtract(request):
    return render(request,"Subtract.html")

def Adding(request):
    scanned = get_object_or_404(Scanned)
    add_value = scanned.Add()
    print(f"Added value : {add_value}")
    if request.method == "POST":
        scanned.save()
        time.sleep(5)
        return redirect("/")
    return render(request,"adding.html",{"num":scanned})

def Subtracting(request):
    scanned = get_object_or_404(Scanned)
    Subtract_value = scanned.Subtract()
    print(f"Subtracted value : {Subtract_value}")
    if request.method == "POST":
        scanned.save()
        time.sleep(5)
        return redirect("/")
    return render(request,"subtracting.html",{"num":scanned})

def Contact(request):
    return render(request,"contactus.html")

def About(request):
    return render(request,"aboutus.html")

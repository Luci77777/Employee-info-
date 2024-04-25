from django.shortcuts import render,redirect
from .models import *


def peoples(request):
    peoples=[
        {'name':'Harshit','age':22},
        {'name':'Vishal','age':25},
        {'name':'Saksham','age':17},
        {'name':'Mohit','age':23},
        {'name':'Shiv','age':22},
    ]



    return render(request,"index.html",context={'peoples':peoples})



def contact(request):
    return render(request,"contact.html",context={})

def about(request):
    return render(request,"about.html")

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'main.html')

def chart1(request):
    return render(request,'chart1.html')

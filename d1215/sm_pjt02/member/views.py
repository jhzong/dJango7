from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return render(request,'member/login.html')

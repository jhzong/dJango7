from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse

def login(request):
    return render(request,'member/login.html')
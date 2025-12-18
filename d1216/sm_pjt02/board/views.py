from django.shortcuts import render, redirect

def list(request):
    return render(request,'board/list.html')

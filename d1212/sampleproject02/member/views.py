from django.shortcuts import render, redirect
from member.models import Member
from django.http import HttpResponse

# 로그인
def login(request):
    return render(request,'member/login.html')

# 로그아웃
def logout(request):
    return render(request,'member/login.html')
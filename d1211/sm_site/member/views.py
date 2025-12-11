from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse# app_name방식
from member.models import Member

# 로그인
def login(request):
    if request.method=='GET':
        return render(request,'member/login.html')
    elif request.method=='POST':
        id=request.POST.get('id')
        pw=request.POST.get('pw')
        print('post입력 :',id,pw)
        qs=Member.objects.filter(id=id,pw=pw)
        if qs:
            print('아이디 and 비번 일치')
            context={'error':'1'}
            return render(request,'member/login.html',context)
        else:
            print('아이디 and 비번 불일치')
            context={'error':'0'}
            return render(request,'member/login.html',context)

# 회원리스트
def list(request):
    qs=Member.objects.all().order_by('-mdate')
    context={'list':qs}
    return render(request,'member/list.html',context)

# 회원등록
def write(request):
    if request.method=='GET':
        return render(request, 'member/write.html')
    elif request.method=='POST':
        id=request.POST.get('id')
        pw=request.POST.get('pw')
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        gender=request.POST.get('gender')
        hobby=request.POST.get('hobby')
        
        Member.objects.create(id=id,pw=pw,name=name,phone=phone,gender=gender,hobby=hobby)
        # qs=(id=id,pw=pw,name=name,phone=phone,gender=gender,hobby=hobby)
        # qs.save()
        
        print('post확인 : ',id)
        return redirect('/')

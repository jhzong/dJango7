from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse# app_name방식
from member.models import Member

# 로그아웃
def logout(request):
    # session 삭제
    request.session.clear()
    context={"error":"-1"}
    return render(request,'member/login.html',context)

# 로그인
def login(request):
    if request.method=='GET':
        # 쿠키읽기
        cook_id=request.COOKIES.get("cook_id","")
        context={"cook_id":cook_id}
        
        return render(request,'member/login.html',context)
    elif request.method=='POST':
        id=request.POST.get('id')
        pw=request.POST.get('pw')
        cook_keep=request.POST.get('cook_keep')
        print('post입력 :',id,pw)
        qs=Member.objects.filter(id=id,pw=pw)
        if qs:
            print('아이디 and 비번 일치')
            # session저장
            # ['key']=value
            request.session['session_id']=id
            context={'error':'1'}
            response=render(request,'member/login.html',context)
            # 쿠키저장/삭제
            if cook_keep:# cook_keep 있을때 저장
                response.set_cookie("cook_id",id,max_age=60*60*24*30)
            else:# cook_keep 없을때 삭제
                response.delete_cookie("cook_id")
            return response
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

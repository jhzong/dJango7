from django.shortcuts import render
from .models import Member

# 로그인 함수----------------------------------------------------------------------
def login(request):
    if request.method=='GET':
        return render(request, 'member/login.html')
    if request.method=='POST':
        id=request.POST.get('id')
        pw=request.POST.get('pw')
        # try:
        #     id=request.POST['id']
        #     pw=request.POST['pw']
        # except:
        #     id=None
        #     pw=None
        qs=Member.objects.filter(id=id,pw=pw)
        # try:
        #     qs=Member.objects.get(id=id,pw=pw)
        # except:
        #     qs=None
        if qs:
            request.session['session_id']=id # 세션추가
            request.session['session_name']=qs[0].name # 세션추가
            context={'flag':'1'}
        else:
            context={'flag':'0'}
        return render(request, 'member/login.html',context)


# 로그아웃 함수----------------------------------------------------------------------
def logout(request):
    request.session.clear()
    context={'flag':'-1'}
    return render(request,'member/login.html',context)
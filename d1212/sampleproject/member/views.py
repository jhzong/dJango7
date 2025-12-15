from django.shortcuts import render, redirect
from member.models import Member

# 로그인
def login(request):
    if request.method=='GET':
        # 쿠키 읽어와서 context에 저장해 전송
        cook_id=request.COOKIES.get('cook_id','')# 쿠키 없으면 공백
        context={'cook_id':cook_id}
        return render(request, 'member/login.html',context)
    elif request.method=='POST':
        id=request.POST.get('id')
        pw=request.POST.get('pw')
        login_keep=request.POST.get('login_keep')
        # id,pw를 활용해 로그인체크
        qs=Member.objects.filter(id=id,pw=pw)
        if qs:
            print("id,pw일치:",id,pw)
            # session에 저장
            request.session['session_id']=id
            request.session['session_name']=qs[0].name
            context={"state_code":"1"}
            response=render(request, 'member/login.html', context)
            
            # 쿠키저장
            if login_keep:
                response.set_cookie('cook_id',id)
            # 쿠키삭제
            else:
                response.delete_cookie('cook_id')
        
        else:
            print("id,pw불일치")
            context={"state_code":"0"}
            response=render(request, 'member/login.html', context)
            
        return response


# 로그아웃
def logout(request):
    # 세션 모두 삭제
    request.session.clear()
    context={'state_code':'-1'}
    return render(request,'member/login.html',context)
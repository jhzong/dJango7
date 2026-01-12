from django.shortcuts import render,redirect
from django.http import JsonResponse
from member.models import Member
import json

def logout(request):
    # session 삭제
    request.session.clear()
    
    return redirect('/')

def login(request):
    if request.method=='GET':
        return render(request,"member/login.html")
    elif request.method=='POST':
        id=request.POST.get('id')
        pw=request.POST.get('pw')
        print('넘어온 데이터 :',id,pw)
        
        #id,pw체크
        qs=Member.objects.filter(id=id,pw=pw)
        if qs:
            result=1
            request.session['session_id']=id
            request.session['session_name']=qs[0].name
        else: result=0
            
        context={'result':result}
        return render(request,"member/login.html",context)
        
    

def step03(request):
    return render(request,"member/step03.html")

# id가 존재하는지 확인해 json으로 return
def idCheck(request):
    #db확인
    id=request.GET.get('id','')
    qs=Member.objects.filter(id=id)
    if not qs:
        result='사용가능'
    else:
        result='사용불가'
    
    context={'result':result}
    return JsonResponse(context)

# json으로 data 넘기기
def userAll(request):
    # db확인
    print('id :',request.GET.get('id',''))
    print('name :',request.GET.get('name',''))
    qs=Member.objects.all()
    l_qs=list(qs.values())
    # print("l_qs 데이터 형태 : ",l_qs)
    context = {'arrey':l_qs}
    return JsonResponse(context)

# json으로 data 넘기기
# def userInsert(request):
#     # db확인
#     # request.POST.get('id','')
#     if request.method=='POST':
#         body=json.loads(request.body)
#         id=body.get('id')
#         print('id :',id)
        
#         qs=Member.objects.all()
#         l_qs=list(qs.values())
#         context = {'arrey':l_qs}
#         return JsonResponse(context)

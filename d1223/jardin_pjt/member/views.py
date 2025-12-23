from django.shortcuts import render
from django.http import JsonResponse
from member.models import Member

def login(request):
    if request.method=='GET':
        return render(request,"member/login.html")
    elif request.method=='POST':
        id=request.POST.get('id')
        pw=request.POST.get('pw')
        print('넘어온 데이터 :',id,pw)
        return render(request,"member/login.html")
        
    

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

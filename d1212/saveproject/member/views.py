from django.shortcuts import render, redirect

def login(request):
    if request.method=='GET':
        cook_id=request.COOKIES.get('cook_id','')
        context={'cook_id':cook_id}
        return render(request, 'member/login.html',context)
    elif request.method=='POST':
        id=request.POST.get('id')
        pw=request.POST.get('pw')
        login_keep=request.POST.get('login_keep')
        # 쿠키검색
        print('모든 쿠키 읽기 : ',request.COOKIES)
        
        # 쿠키저장
        response=redirect('index')
        if login_keep:
            print('쿠키저장')
            response.set_cookie('cook_id',id)
        else:
            print('쿠키삭제')
            response.delete_cookie('cook_id')
        print('post입력정보:',id,pw,login_keep)
        return response

# # 견본
# def login(request):
    # if request.method=='GET':
    #     # 쿠키검색
    #     cooksave_id=request.COOKIES.get('cook_id','')# 쿠키 있으면 읽어오기
    #     context={'cook_id':cook_id}
    #     return render(request,'member/login.html',context)
    # elif request.method=='POST':
    #     id=request.POST.get('id')
    #     pw=request.POST.get('pw')
    #     login_keep=request.POST.get('login_keep')# getlist()
        
    #     # 쿠키저장
    #     response=redirect('index')# response 없어도 잘 찾아감
    #     if login_keep:# id저장을 채크했을 때
    #         print('id저장이 채크 됨')
    #         ## 쿠키에 id를 저장시킴
    #         response.set_cookie('cook_id',id,max_age=60*60*24*30)
    #         # cook_id=id 30days
    #     else:
    #         print('id저장이 채크 안됨')
        
    #     return response

from django.shortcuts import render

def index(request):
    # # 쿠키 검색 request
    # cook_info=request.COOKIES
    # print('쿠키모든정보:',cook_info)
    # cook_id=request.COOKIES.get('cook_id','')# cook_id가 있으면 불러오고 없으면 ''
    # print('cook_id 정보:',cook_id)
    
    response=render(request, 'index.html')
    # 쿠키저장 response
    # 유지시간이 없으면, 브라우저 종료시 사라짐.(설정된 시간동안 유지)
    # if not cook_id:# 쿠키정보가 없을때 저장
    #     response.set_cookie('smsite_connect','ok')# =>cook_id=aaa, all_day
    #     response.set_cookie('ip','127.0.0.1',max_age=60*60*24)# =>cook_pw=1111, all_day
    #     # response.set_cookie('변수','값',max_age='유지시간')
    return response

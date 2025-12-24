from django.shortcuts import render
from customer.models import Board
from django.core.paginator import Paginator

def clist(request):
    # 검색부분--------------------------------------------
    category=request.GET.get('category','')
    search=request.GET.get('search','')
    # //검색부분------------------------------------------
    if not search:
        qs=Board.objects.all().order_by('-bgroup','bstep')
    else:    
        qs=Board.objects.filter(category=category,search=search)
    
    # 하단 페이지넘버링-------------------------------------
    # paginator는 요청페이지 번호가 있어야함.
    # 요청페이지 넘버:int타입
    page=int(request.GET.get('page',1))# 없으면 default=1
    paginator=Paginator(qs,10)
    list_qs=paginator.get_page(page)
    # //하단 페이지넘버링-----------------------------------
    
    context={'list':list_qs,'page':page}
    return render(request,'customer/clist.html',context)

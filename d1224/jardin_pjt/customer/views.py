from django.shortcuts import render
from customer.models import Board
from django.core.paginator import Paginator
from django.db.models import Q,F

# 상세페이지
def cview(request, bno):
    qs=Board.objects.get()
    return render(request,'customer/cview.html')

def clist(request):
    # 검색부분--------------------------------------------
    category=request.GET.get('category','')
    search=request.GET.get('search','')
    print('넘어온 데이터 => ',category,search)
    # //검색부분------------------------------------------
    
    if not search:
        qs=Board.objects.all().order_by('-bgroup','bstep')
    else:
        if category == 'btitle':
            qs=Board.objects.filter(btitle__contains=search)
        elif category == 'bcontent':
            qs=Board.objects.filter(bcontent__contains=search)
        elif category == 'all':
            qs=Board.objects.filter(Q(btitle__contains=search)|Q(bcontent__contains=search))
            
    
    # 하단 페이지넘버링-------------------------------------
    # paginator는 요청페이지 번호가 있어야함.
    # 요청페이지 넘버:int타입
    page=int(request.GET.get('page',1))# 없으면 default=1
    paginator=Paginator(qs,10)
    list_qs=paginator.get_page(page)
    # //하단 페이지넘버링-----------------------------------
    
    context={'list':list_qs,'page':page,'category':category,'search':search}
    return render(request,'customer/clist.html',context)

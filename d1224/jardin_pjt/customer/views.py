from django.shortcuts import render,redirect
from customer.models import Board
from member.models import Member
from django.core.paginator import Paginator
from django.db.models import Q,F,Sum,Count

# 글쓰기페이지
def cwrite(request):
    if request.method=="GET":
        return render(request,'customer/cwrite.html')
    elif request.method=='POST':
        id=request.session['session_id']
        member=Member.objects.get(id=id)
        btitle=request.POST.get('btitle')
        bcontent=request.POST.get('bcontent')
        bfile=request.FILES.get('bfile')
        # db에 저장
        qs=Board.objects.create(member=member,btitle=btitle,bcontent=bcontent,bfile=bfile)
        qs.bgroup=qs.bno
        qs.save()
        return redirect('/customer/clist/')

# 상세페이지
def cview(request, bno):
    qs=Board.objects.get(bno=bno)
    
    # 이전/다음글로 이동
    # 현재정렬 설정 => bgroup은 역순, bstep은 순차
    # 이전글
    prev_qs=Board.objects.filter(bgroup__lt=qs.bgroup).order_by('-bgroup','bstep').first()
    print('이전글=>',prev_qs)
    # 답글달기 기능이 있을때 이전글 query문
    # pre_qs = Board.objects.filter(Q(bgroup__lt=qs[0].bgroup,bstep__lte=qs[0].bstep)|Q(bgroup=qs[0].bgroup,bstep__gt=qs[0].bstep)).order_by("-bgroup","bstep").first()
    
    # 다음글
    next_qs=Board.objects.filter(bgroup__gt=qs.bgroup).order_by('bgroup','-bstep').first()
    print('다음글=>',next_qs)
    # 답글달기 기능이 있을때 다음글 query문
    # next_qs=Board.objects.filter(Q(bgroup__gt=qs[0].bgroup,bstep__gte=qs[0].bstep)|Q(bgroup=qs[0].bgroup,bstep__lt=qs[0].bstep)).order_by("bgroup","-bstep").first(
    
    context={'c':qs,'prev_c':prev_qs,'next_c':next_qs}
    return render(request,'customer/cview.html',context)

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

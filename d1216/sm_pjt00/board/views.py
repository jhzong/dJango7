from django.shortcuts import render, redirect
from board.models import Board
from member.models import Member
from django.db.models import F,Q
from django.core.paginator import Paginator #

# 게시판 목록(+페이지 넘버링)---------------------------------------
def list(request):
    qs=Board.objects.all().order_by('-bgroup','bstep')
    # 하단 페이지 넘버링(qs,10)->1페이지 10개씩
    paginator=Paginator(qs,10)# 101->11page
    # 현제페이지 넘김
    page=int(request.GET.get('page',1))
    list_qs=paginator.get_page(page)# 1page에 게시글 10개 전달
    
    context={'list':list_qs,'page':page}
    return render(request,'board/list.html',context)

# 게시물 쓰기-----------------------------------------------------
def write(request):
    if request.method=='GET':
        return render(request,'board/write.html')
    elif request.method=='POST':
        id=request.session.get('session_id')
        member_qs=Member.objects.get(id=id)
        btitle=request.POST.get('btitle')
        bcontent=request.POST.get('bcontent')
        bfile=request.FILES.get('bfile')
        # 저장
        qs=Board.objects.create(btitle=btitle,bcontent=bcontent,member=member_qs,bfile=bfile)
        
        # bgroup과
        qs.bgroup=qs.bno
        qs.save()
        
        context={'flag':'1'}
        return render(request,'board/write.html',context)

# 게시물 상세-----------------------------------------------------
def view(request,bno):
    qs=Board.objects.filter(bno=bno)# bno에 해당하는 게시글 가져오기
    # 조회수 증가
    qs.update(bhit=F('bhit')+1)# 데이터를 검색후 update,delete : F
    context={'board':qs[0]}
    return render(request,'board/view.html',context)

# 게시물 삭제-----------------------------------------------------
def delete(request,bno):
    qs=Board.objects.get(bno=bno)# bno에 해당하는 게시글 가져오기
    qs.delete()
    return redirect('/board/list/')

# 게시물 수정-----------------------------------------------------
def update(request,bno):
    if request.method=='GET':
        qs=Board.objects.get(bno=bno)
        context={'board':qs}
        return render(request,'board/update.html',context)
    elif request.method=='POST':
        id=request.session.get('session_id')
        member=Member.objects.get(id=id)
        btitle=request.POST.get('btitle')
        bcontent=request.POST.get('bcontent')
        bfile=request.FILES.get('bfile')
        # 수정
        qs=Board.objects.get(bno=bno)
        qs.btitle=btitle
        qs.bcontent=bcontent
        
        if bfile:
            qs.bfile=bfile
        qs.save()
        return redirect(f'/board/view/{bno}/')
    
    # qs.delete()
    # return redirect('/board/list/')
from django.shortcuts import render, redirect
from board.models import Board
from member.models import Member


# 게시판 목록-----------------------------------------------------
def list(request):
    qs=Board.objects.all().order_by('-bgroup','bstep')
    context={'list':qs}
    return render(request,'board/list.html',context)

# 게시물 쓰기-----------------------------------------------------
def write(request):
    if request.method=='GET':
        return render(request,'board/write.html')
    if request.method=='POST':
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
    qs=Board.objects.get(bno=bno)# bno에 해당하는 게시글 가져오기
    context={'board':qs}
    return render(request,'board/view.html',context)

# 게시물 삭제-----------------------------------------------------
def delete(request,bno):
    qs=Board.objects.get(bno=bno)# bno에 해당하는 게시글 가져오기
    qs.delete()
    return redirect('/board/list/')
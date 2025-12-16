from django.shortcuts import render,redirect
from member.models import Member
from board.models import Board

# <게시글 목록>---------------------------------------------
def list(request):
    qs=Board.objects.all().order_by('-bno')
    print(qs)
    context={"list":qs}
    return render(request,'board/list.html',context)

# <게시글 쓰기>---------------------------------------------
def write(request):
    if request.method=="GET":
        return render(request,'board/write.html')
    elif request.method=="POST":
        btitle=request.POST.get('title')
        bcontent=request.POST.get('content')
        id=request.session['session_id']
        qs=Member.objects.get(id=id)
        qs2=Board.objects.create(btitle=btitle,bcontent=bcontent,member=qs)
        qs2.save()
        context={'flag':'1'}
        return render(request,'board/write.html',context)

# <게시글 상세보기>---------------------------------------------
def view(request, bno):
    qs=Board.objects.get(bno=bno)
    context={'detail':qs}
    return render(request,'board/view.html',context)

# <게시글 삭제(상세보기)>----------------------------------------
def delete(request, bno):
    qs=Board.objects.get(bno=bno)
    qs.delete()
    return redirect('/board/list/')

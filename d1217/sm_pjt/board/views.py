from django.shortcuts import render,redirect
from board.models import Board
from comment.models import Comment
from member.models import Member
from django.db.models import F,Q
from django.core.paginator import Paginator
import requests
import json
import pprint

# 차트 그리기
def chart(request):
    return render(request,'board/chart.html')


# 게시판 답글달기
def reply(request,bno):
    if request.method == 'GET':
        # 게시글 가져오기
        qs = Board.objects.get(bno=bno)
        context = {'board':qs}
        return render(request,'board/reply.html',context)
    elif request.method == 'POST':
        # 답글저장
        bgroup = request.POST.get('bgroup')
        bstep = int(request.POST.get('bstep'))
        bindent = int(request.POST.get('bindent'))
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        id = request.session.get('session_id')
        member = Member.objects.get(id=id)
        bfile = request.FILES.get('bfile','')
        # 1. 답글달기 : 우선 같은 그룹에 있는 게시글의 bstep 1씩 먼저 증가
        board_qs = Board.objects.filter(bgroup=bgroup,bstep__gt = bstep)
        board_qs.update(bstep=F('bstep')+1) # F함수 : 검색된 그 컬럼에만 값을 적용
        
        # 2. 답글저장
        Board.objects.create(btitle=btitle,bcontent=bcontent,member=member,bgroup=bgroup,\
            bstep=bstep+1,bindent=bindent+1,bfile=bfile)
        
        
        context = {'flag':1}
        return render(request,'board/reply.html',context)


# 게시판 수정
def update(request,bno):
    if request.method == 'GET':
        # 게시글 가져오기
        qs = Board.objects.get(bno=bno)
        context = {'board':qs}
        return render(request,'board/update.html',context)
    elif request.method == 'POST':
        id = request.session.get('session_id')
        member = Member.objects.get(id=id)
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        bfile = request.FILES.get('bfile')
        # 수정
        qs = Board.objects.get(bno=bno)
        qs.btitle = btitle
        qs.bcontent = bcontent
        if bfile: qs.bfile = bfile
        qs.save()    
        return redirect(f'/board/view/{bno}/')    
                
# 게시판 삭제
def delete(request,bno):
    # 게시글 가져오기
    qs = Board.objects.get(bno=bno)
    qs.delete()
    context = {'flag':2}
    return redirect("/board/list/")

# 게시판 상세보기 - 해당 하단댓글도 함께 가져올수 있음.
def view(request,bno):
    # 게시글 가져오기
    qs = Board.objects.filter(bno=bno)
    # 하단댓글
    c_qs = Comment.objects.filter(board=qs[0])
    # 조회수 1증가
    # 조회를 한후 조회된 데이터들을 update,delete : F
    qs.update(bhit = F('bhit') + 1 )
    context = {'board':qs[0],'clist':c_qs}
    return render(request,'board/view.html',context)

# 게시판 상세보기 - 해당 하단댓글도 함께 가져올수 있음.
def view2(request,bno):
    print("bno : ",bno)
    # 게시글 가져오기
    qs = Board.objects.filter(bno=bno)
    # 하단댓글
    c_qs = Comment.objects.filter(board=qs[0]).order_by('-cno')
    context = {'board':qs[0],'clist':c_qs}
    return render(request,'board/view2.html',context)


# 게시판 리스트
def list(request):
    # 게시글 모두 가져오기
    qs = Board.objects.all().order_by('-bgroup','bstep')
    # 하단 넘버링 (qs,10) -> 1페이지 10개씩
    paginator = Paginator(qs,10)  # 101 -> 11
    # 현재페이지 넘김.
    page = int(request.GET.get('page',1))
    list_qs = paginator.get_page(page) # 1page -> 게시글 10개를 전달
    
    context = {'list':list_qs,'page':page}
    return render(request,'board/list.html',context)

#--------------------------------------------------------------------------------------
## 상단에 추가
# import requests
# import json
# import pprint

# 공공데이터 리스트 - API(관광정보)
def list2(request):
    # 공공데이터 접속
    public_key='29b0b931e96abea5be6407185e36ed3cb76294a1ee46ef38a702ee3acf6d5c79'
    # page_no=requests.GET.get('page_no')
    page_no=1
    url=f"https://apis.data.go.kr/B551011/PhotoGalleryService1/galleryList1?serviceKey={public_key}&numOfRows=10&pageNo={page_no}&MobileOS=ETC&MobileApp=AppTest&arrange=A&_type=json"
    # url의 모든 태그를 가져옴
    # 공공데이터 정보 가져오기
    rel=requests.get(url)
    # 파일변환:str->json
    json_data=json.loads(rel.text)
    p_list=json_data['response']['body']['items']['item']
    print('[json데이터]=>',p_list[0])    
    context = {'result':'성공','list':p_list}
    return render(request,'board/list2.html',context)
#--------------------------------------------------------------------------------------
# 공공데이터 리스트 - API(영화정보)
def list3(request):
    # 공공데이터 접속
    public_key='354a8a2eb23f2ffd9a5d4e6e4f6d3cc7'
    # # page_no=requests.GET.get('page_no')
    # page_no=1
    url=f"http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key={public_key}&targetDt=20251130"
    # url의 모든 태그를 가져옴
    # 공공데이터 정보 가져오기
    rel=requests.get(url)
    # 파일변환:str->json
    json_data=json.loads(rel.text)
    p_list=json_data['boxOfficeResult']['dailyBoxOfficeList']
    print('[json데이터]=>',p_list[0])    
    context = {'list':p_list}
    return render(request,'board/list3.html',context)
#--------------------------------------------------------------------------------------

# 게시판 글쓰기
def write(request):
    if request.method == 'GET':
        return render(request,'board/write.html')
    elif request.method == 'POST':
        id = request.session.get('session_id')
        member_qs = Member.objects.get(id=id)
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        bfile = request.FILES.get('bfile','')
        # bgroup 값을 입력
        qs = Board.objects.create(btitle=btitle,bcontent=bcontent,member=member_qs,bfile=bfile)
        qs.bgroup = qs.bno
        qs.save()
        context = {'flag':'1'}
        return render(request,'board/write.html',context)
        
from django.shortcuts import render,redirect
from board.models import Board
import datetime


def write(request):
    if request.method=="GET":
        return render(request, 'board/write.html')
    elif request.method=="POST":
        btitle=request.POST.get('btitle')
        bfile=request.FILES.get('bfile') # 파일은 POST가 아니라 FILES
        
        # # 이름변경
        # bfile=f'{datetime.datetime.now().microsecond}_{bfile}'
        
        print('post btitle정보 :',btitle)
        print('post bfile정보 :',bfile)
        print('날짜 :',datetime.datetime.now())
        print('날짜 :',datetime.datetime.now().microsecond)
        
        # 파일저장
        qs=Board(btitle=btitle,bfile=bfile)
        qs.save()
        
        return render(request, 'board/write.html')

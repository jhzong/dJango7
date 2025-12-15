from django.shortcuts import render
from django.http import HttpResponse
from .models import Board
from member.models import Member

def list(request):
    qs=Board.objects.all().order_by('-bno')
    print(qs)
    context={'list':qs}
    return render(request,'board/list.html',context)

def write(request):
    return render(request,'board/write.html')
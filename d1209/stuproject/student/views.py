from django.shortcuts import render
from django.http import HttpResponse

def write(request):
    # return HttpResponse('Hello') 직접 html 출력
    return render(request,'write.html')
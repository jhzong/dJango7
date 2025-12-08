from django.shortcuts import render

def write(request):
    # render - html페이지 열기
    return render(request,'write.html')

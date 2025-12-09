from django.shortcuts import render
from django.http import HttpResponse

def write(request):
    # return HttpResponse('Hello')
    return render(request,'student/write.html')

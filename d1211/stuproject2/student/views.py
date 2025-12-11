from django.shortcuts import render, redirect
from django.urls import reverse
from student.models import Student

def write(request):
    if request.method=='GET':
        return render(request,'student/write.html')
    elif request.method=='POST':
        name=request.POST.get('name')
        age=request.POST.get('age')
        grade=request.POST.get('grade')
        gender=request.POST.get('gender')
        hobby=request.POST.getlist('hobby')
        
        qs=Student(name=name,age=age,grade=grade,gender=gender,hobby=hobby)
        qs.save()

        return render(request,'student/write.html')
        # return redirect(reverse('student:list'))

def list(request):
    qs=Student.objects.all().order_by('-sno')
    context={'list':qs}
    return render(request,'student/list.html',context)

def view(request):
    return render(request,'student/view.html')
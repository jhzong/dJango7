from django.shortcuts import render, redirect
from django.urls import reverse
from student.models import Student

# write함수
def write(request):
    if request.method=='GET':
        return render(request,'student/write.html')
    elif request.method=='POST':
        name=request.POST.get('name')
        age=request.POST.get('age')
        grade=request.POST.get('grade')
        gender=request.POST.get('gender')
        hobby=request.POST.getlist('hobby')
        
        Student(name=name,age=age,grade=grade,gender=gender,hobby=hobby).save()
        return redirect(reverse('student:list'))
        # return render(request,'student/write.html')

# list함수
def list(request):
    qs=Student.objects.all().order_by('-sno')
    context={'list':qs}
    return render(request,'student/list.html',context)

# view함수
def view(request, sno):
    qs=Student.objects.get(sno=sno)
    context={'student':qs}
    return render(request,'student/view.html',context)
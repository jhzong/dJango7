from django.shortcuts import render, redirect# redirect추가
from . import views
from django.http import HttpResponse
from django.urls import reverse # 구문추가
from student.models import Student # Student를 import

# write(등록)
def write(request):
    if request.method=='GET':
        return render(request, 'student/write.html')
    elif request.method=='POST':
        # sno=request.POST.get('sno')# AuteField여서 생략가능
        name=request.POST.get('name')
        age=request.POST.get('age')
        grade=request.POST.get('grade')
        gender=request.POST.get('gender')
        hobby=request.POST.getlist('hobby')
        # models.py-Student에 저장(qs.save()/Table.objects.create()/Table().save())
        qs=Student(name=name,age=age,grade=grade,gender=gender,hobby=hobby)
        qs.save()
        print('post 확인 :',name)
        # return render(request,'student/list.html')# url 주소는 그대로 studnt/write로 유지됨
        return redirect(reverse('student:list'))# url주소를 바꿔줌

# list(리스트)
def list(request):
    qs=Student.objects.all().order_by('-sno')
    context={'list':qs}# 1개는 변수, 여러개는 list
    return render(request, 'student/list.html',context)

# view(상세보기)
def view(request,sno):
    qs=Student.objects.get(sno=sno)
    context={'stu':qs}
    return render(request, 'student/view.html', context)

# delete(삭제)
def delete(request, sno):
    qs=Student.objects.get(sno=sno)
    qs.delete() # 삭제문
    return redirect(reverse('student:list'))

# update(수정)
def update(request, sno):
    if request.method=='GET':
        qs=Student.objects.get(sno=sno)
        context={'stu':qs}
        return render(request, 'student/update.html', context)
    elif request.method=='POST':
        # sno=request.POST.get('sno')# AuteField여서 생략가능
        name=request.POST.get('name')
        age=request.POST.get('age')
        grade=request.POST.get('grade')
        gender=request.POST.get('gender')
        hobby=request.POST.getlist('hobby')
        # models.py-Student에 저장(qs.save()/Table.objects.create()/Table().save())
        qs=Student(name=name,age=age,grade=grade,gender=gender,hobby=hobby)
        qs.save()
        print('post 확인 :',name)
        # return render(request,'student/list.html')# url 주소는 그대로 studnt/write로 유지됨
        return redirect(reverse('student:list'))# url주소를 바꿔줌
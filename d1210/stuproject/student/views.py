from django.shortcuts import render, redirect
from django.urls import reverse
from student.models import Student # models에서 import
# write함수
def write(request):
    if request.method == 'GET':
        return render(request, 'student/write.html')
    elif request.method == 'POST':
        # form에서 넘어온 데이터 처리
        name=request.POST.get("name")
        age=request.POST.get("age")
        grade=request.POST.get("grade")
        gender=request.POST.get("gender")
        hobby=request.POST.getlist("hobby")
        # hobby=','.join(hobby) 배열(리스트타입)을 문자열로 변환
        # 리스트타입을 문자열항목에 저장하면 자동으로 변환됨
        # (1)
        # qs=Student(name=name,age=age,grade=grade,gender=gender)
        # qs.save()
        # (2)
        Student(name=name,age=age,grade=grade,gender=gender,hobby=hobby).save()
        # (3)
        # create.objects.Student(name=name,age=age,grade=grade,gender=gender)
        print("이름 :",name)
        print("취미 :",hobby)
        
        return redirect(reverse('student:list'))

# list함수
def list(request):
    # db 명령어 - select,insert,update,delete
    qs=Student.objects.all().order_by('-sno','name')
    context = {"list":qs}# 변수
    # qs1=Student.objects.get(name='홍길동')(개별)
    # qs2=Student.objects.get(name='유관순')(개별)
    return render(request, 'student/list.html',context)

# view함수
def view(request,sno):
    # age = request.GET['age']# 데이터 없으면 에러(restful 나중에 공부)
    # print("넘어온 데이타 sno :",sno)
    qs=Student.objects.get(sno=sno)
    context={"student":qs}
    return render(request, 'student/view.html', context)

# delete함수
def delete(request):
    
    return render(request, 'student/delete.html')
from django.shortcuts import render, redirect

def login(request):
    if request.method=='GET':
        return render(request, 'member/login.html')
    elif request.method=='POST':
        id=request.POST.get('id')
        pw=request.POST.get('pw')
        id_save=request.POST.get('id_save')
        
        
        return redirect('index')

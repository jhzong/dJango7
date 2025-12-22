from django.shortcuts import render
from django.http import JsonResponse
from home.models import ChartData

def index(request):
    return render(request,'index.html')

def chart1(request):
    return render(request,'chart1.html')

def chart_json1(request):
    input_data=request.GET.get('input_data')
    qs=ChartData.objects.all()
    
    labels=[]
    values=[]
    
    for i in qs:
        labels.append(i.cyear)
        values.append(i.cdata)
    
    context={'labels':labels,'values':values}
    return JsonResponse(context)

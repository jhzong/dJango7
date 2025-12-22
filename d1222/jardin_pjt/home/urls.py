
from django.urls import path,include
from . import views

app_name=''
urlpatterns = [
    path('',views.index,name='index'),
    path('chart1/',views.chart1,name='chart1'),
]

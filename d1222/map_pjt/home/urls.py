from django.urls import path, include
from . import views

app_name=''
urlpatterns = [
    path('', views.index, name='index'),
    path('chart1/', views.chart1, name='chart1'),
    path('chart_json1/', views.chart_json1, name='chart_json1'),
]

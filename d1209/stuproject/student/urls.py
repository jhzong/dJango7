from django.urls import path, include
from . import views

app_name='student'
urlpatterns = [
    # write 페이지로 연결
    path('write/', views.write, name='write'),
]

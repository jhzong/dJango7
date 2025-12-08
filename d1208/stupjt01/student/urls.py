from django.urls import path,include
from . import views

app_name='student'# 닉네임/별칭 정해주기
urlpatterns = [
    # url을 write 페이지로 넘겨줌, write 함수 호출
    path('write/', views.write, name='write'),
]

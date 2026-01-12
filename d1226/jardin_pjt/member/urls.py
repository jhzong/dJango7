
from django.urls import path,include
from . import views

app_name='member'
urlpatterns = [
    # html return
    path('step03/',views.step03,name='step03'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    # id가 존재하는지 확인해 json으로 return
    path('idCheck/',views.idCheck,name='idCheck'),
    # 리엑트와 연결
    path('userAll/',views.userAll,name='userAll'),
    # path('userInsert/',views.userInsert,name='userInsert'),
]

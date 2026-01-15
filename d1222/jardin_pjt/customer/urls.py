from django.urls import path,include
from . import views

app_name='customer'
urlpatterns = [
    # 리엑트
    path('clistJson/', views.clistJson, name='clistJson'),
    path('cwriteJson/', views.cwriteJson, name='cwriteJson'),
    path('cdeleteJson/<int:bno>/', views.cdeleteJson, name='cdeleteJson'),
    # path('cviewJson/<int:bno>/', views.cviewJson, name='cviewJson'),
    
    # html리턴
    path('clist/', views.clist, name='clist'),
    path('cwrite/', views.cwrite, name='cwrite'),
    path('cview/<int:bno>/', views.cview, name='cview'),
    # 좋아요
    path('clikes/', views.clikes, name='clikes'),
]


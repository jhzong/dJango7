from django.urls import path, include
from . import views

app_name='student03'
urlpatterns = [
    path('write/', views.write, name='write'),
]

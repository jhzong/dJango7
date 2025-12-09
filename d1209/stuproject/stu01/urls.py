from django.contrib import admin
from django.urls import path, include

# 다른앱에있는 urls파일을 연결
urlpatterns = [
    path('admin/', admin.site.urls),
    # student app의 urls로 연결
    path('student/', include('student.urls')),
    # home으로 연결
    path('', include('home.urls')),
]

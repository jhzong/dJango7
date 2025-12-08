from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    # url을 stendent로 넘겨줌
    path('student/', include('student.urls')),
]

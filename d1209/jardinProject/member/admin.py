from django.contrib import admin
# member app에서 models 파일안의 Member class 가져옴
from member.models import Member

# Register your models here.
admin.site.register(Member)
from django.db import models

# 테이블 생성-sql구문 python명령어로 대체
# table을 생성하면 id는 AutoField로 생성됨(default)
# table명은 student_student로 생성됨
class Student(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    age=models.IntegerField(default=1)
    grade=models.IntegerField(default=1)
    gender=models.CharField(max_length=10)
    hobby=models.CharField(max_length=100,default='게임')
    
        
# 객체출력 - 주소값,__str__객체를 문자열로 출력
    def __str__(self):
        return f"{self.sno},{self.name},{self.age},{self.grade},{self.gender}"

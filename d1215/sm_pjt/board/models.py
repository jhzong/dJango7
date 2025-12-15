from django.db import models
from member.models import Member

class Board(models.Model):
    bno=models.AutoField(primary_key=True)
    # id -> ORM방식:객체저장이 가능
    member=models.ForeignKey(Member,on_delete=models.DO_NOTHING,null=True) # id
    btitle=models.CharField(max_length=1000)
    bcontent=models.TextField()
    bgroup=models.IntegerField(default=0)
    bstep=models.IntegerField(default=0)
    bindent=models.IntegerField(default=0)
    bhit=models.IntegerField(default=0)
    bfile=models.CharField(max_length=100,default='')
    bdate=models.DateTimeField(auto_now=True)
    
    # 댓글달기파트
    # bgroup,bstep,bindent
    # 파일첨부
    # bfile
    
    def __str__(self):
        return f"{self.bno},{self.btitle},{self.member.id},{self.bdate}"
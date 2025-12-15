from django.db import models
from member.models import Member

class Board(models.Model):
    bno=models.AutoField(primary_key=True)
    member=models.ForeignKey(Member,on_delete=models.DO_NOTHING)
    btitle=models.CharField(max_length=1000)
    bcontent=models.TextField()
    bhit=models.IntegerField(default=0)
    bdate=models.DateTimeField(auto_now=True)
    bfile=models.CharField(max_length=100,default='')
    # bgroup,bstep,bindent-댓글
    
    def __str__(self):
        return f"{self.bno},{self.btitle},{self.member.id},{self.bdate}"
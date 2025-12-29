from django.db import models

class Payment(models.Model):
    aid=models.CharField(max_length=100)

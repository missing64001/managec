from django.db import models

# Create your models here.
class Play(models.Model):
    create_time = models.DateTimeField(verbose_name='生成时间',auto_now_add=True,blank=True,null=True)
    finished_time = models.DateTimeField(verbose_name='完成时间',auto_now=True,blank=True,null=True)
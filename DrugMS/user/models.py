from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class customer5142(models.Model):
    cno = models.CharField(primary_key=True, max_length=10)
    csex = models.CharField(max_length=1, blank=True, null=True)
    cname = models.CharField(max_length=10, blank=True, null=True)
    dill = models.CharField(max_length=10)

    class Meta:
        managed = True
        db_table = '顾客5142'

class staff5142(models.Model):
    ano = models.CharField(primary_key=True, max_length=10)
    aposition = models.CharField(max_length=20, blank=True, null=True)
    aname = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = '员工5142'

class supply5142(models.Model):
    sno = models.CharField(primary_key=True, max_length=10)
    sname = models.CharField(max_length=20)
    schat = models.IntegerField(blank=True, null=True)
    sadress = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = True
        db_table = '供应商5142'


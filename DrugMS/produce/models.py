from django.db import models
from user.models import supply5142
# Create your models here.

class drug5142(models.Model):
    dno = models.CharField(primary_key=True, max_length=10)
    sno = models.ForeignKey(supply5142, models.DO_NOTHING, db_column='sno')
    dname = models.CharField(max_length=20)
    ddate = models.DateTimeField()
    dill = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = '药品5142'

class produce5142(models.Model):
    sno = models.ForeignKey(supply5142, models.DO_NOTHING, db_column='sno')
    dno = models.ForeignKey(drug5142, models.DO_NOTHING, db_column='dno')
    drug_count = models.IntegerField()
    per_s_money = models.IntegerField()
    s_done = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = '制药5142'
        unique_together = (('sno', 'dno'),)
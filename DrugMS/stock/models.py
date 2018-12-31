from django.db import models
from user.models import staff5142,supply5142
from produce.models import drug5142
# Create your models here.
class shop5142(models.Model):
    pno = models.CharField(primary_key=True, max_length=10)
    ano = models.ForeignKey(staff5142, models.DO_NOTHING, db_column='ano')
    pname = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = True
        db_table = '药房5142'

class stock5142(models.Model):
    pno = models.ForeignKey(shop5142, models.DO_NOTHING, db_column='pno')
    dno = models.ForeignKey(drug5142, models.DO_NOTHING, db_column='dno')
    d_count = models.IntegerField()
    per_p_money = models.IntegerField()

    class Meta:
        managed = True
        db_table = '库存5142'
        unique_together = (('pno', 'dno'),)

class bill5142(models.Model):
    dno = models.ForeignKey(drug5142, models.DO_NOTHING, db_column='dno', blank=True, null=True)
    ano = models.ForeignKey(staff5142, models.DO_NOTHING, db_column='ano', blank=True, null=True)
    sno = models.ForeignKey(supply5142, models.DO_NOTHING, db_column='sno')
    drug_b_count = models.IntegerField(blank=True, null=True)
    bno = models.CharField(primary_key=True, max_length=20)
    per_b_money = models.IntegerField(blank=True, null=True)
    id = models.IntegerField(blank=True, null=True)
    s_done = models.IntegerField(blank=True, null=True,default='0')

    class Meta:
        managed = True
        db_table = '进货单5142'
        unique_together = (('dno', 'ano', 'sno'),)
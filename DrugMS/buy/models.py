from django.db import models
from produce.models import drug5142
from user.models import customer5142
from stock.models import shop5142

# Create your models here.
class buy5142(models.Model):
    dno = models.ForeignKey(drug5142, models.DO_NOTHING, db_column='dno')
    cno = models.ForeignKey(customer5142, models.DO_NOTHING, db_column='cno')
    drug_b_count = models.IntegerField(blank=True, null=True)
    per_c_money = models.IntegerField(blank=True, null=True)
    pno = models.ForeignKey(shop5142, models.DO_NOTHING, db_column='pno')
    bdate = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = '购买5142'
        unique_together = (('dno', 'cno', 'pno', 'bdate'),)

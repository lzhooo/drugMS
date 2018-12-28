# # This is an auto-generated Django model module.
# # You'll have to do the following manually to clean this up:
# #   * Rearrange models' order
# #   * Make sure each model has one field with primary_key=True
# #   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
# #   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# # Feel free to rename the models, but don't rename db_table values or field names.
# from __future__ import unicode_literals
#
# from django.db import models
#
#
# class AuthGroup(models.Model):
#     name = models.CharField(unique=True, max_length=80)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_group'
#
#
# class AuthGroupPermissions(models.Model):
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#     permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_group_permissions'
#         unique_together = (('group', 'permission'),)
#
#
# class AuthPermission(models.Model):
#     name = models.CharField(max_length=255)
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
#     codename = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_permission'
#         unique_together = (('content_type', 'codename'),)
#
#
# class AuthUser(models.Model):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.IntegerField()
#     username = models.CharField(unique=True, max_length=150)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     email = models.CharField(max_length=254)
#     is_staff = models.IntegerField()
#     is_active = models.IntegerField()
#     date_joined = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'auth_user'
#
#
# class AuthUserGroups(models.Model):
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_user_groups'
#         unique_together = (('user', 'group'),)
#
#
# class AuthUserUserPermissions(models.Model):
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_user_user_permissions'
#         unique_together = (('user', 'permission'),)
#
#
# class DjangoAdminLog(models.Model):
#     action_time = models.DateTimeField()
#     object_id = models.TextField(blank=True, null=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.SmallIntegerField()
#     change_message = models.TextField()
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'django_admin_log'
#
#
# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)
#
#
# class DjangoMigrations(models.Model):
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'django_migrations'
#
#
# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'django_session'
#
#
# class 5142(models.Model):
#     sno = models.CharField(primary_key=True, max_length=10)
#     sname = models.CharField(max_length=20)
#     schat = models.IntegerField(blank=True, null=True)
#     sadress = models.CharField(max_length=40, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = '供应商5142'
#
#
# class 5142(models.Model):
#     sno = models.ForeignKey(5142, models.DO_NOTHING, db_column='sno')
#     dno = models.ForeignKey(5142, models.DO_NOTHING, db_column='dno')
#     drug_count = models.IntegerField()
#     per_s_money = models.IntegerField()
#     s_done = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = '制药5142'
#         unique_together = (('sno', 'dno'),)
#
#
# class 5142(models.Model):
#     ano = models.CharField(primary_key=True, max_length=10)
#     aposition = models.CharField(max_length=20, blank=True, null=True)
#     aname = models.CharField(max_length=20, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = '员工5142'
#
#
# class 5142(models.Model):
#     pno = models.ForeignKey(5142, models.DO_NOTHING, db_column='pno')
#     dno = models.ForeignKey(5142, models.DO_NOTHING, db_column='dno')
#     d_count = models.IntegerField()
#     per_p_money = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = '库存5142'
#         unique_together = (('pno', 'dno'),)
#
#
# class 5142(models.Model):
#     dno = models.CharField(primary_key=True, max_length=10)
#     sno = models.ForeignKey(5142, models.DO_NOTHING, db_column='sno')
#     dname = models.CharField(max_length=20)
#     ddate = models.DateTimeField()
#     dill = models.CharField(max_length=20)
#
#     class Meta:
#         managed = False
#         db_table = '药品5142'
#
#
# class 5142(models.Model):
#     pno = models.CharField(primary_key=True, max_length=10)
#     ano = models.ForeignKey(5142, models.DO_NOTHING, db_column='ano')
#     pname = models.CharField(max_length=10, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = '药房5142'
#
#
# class 5142(models.Model):
#     dno = models.ForeignKey(5142, models.DO_NOTHING, db_column='dno')
#     cno = models.ForeignKey(5142, models.DO_NOTHING, db_column='cno')
#     drug_b_count = models.IntegerField(blank=True, null=True)
#     per_c_money = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = '购买5142'
#         unique_together = (('dno', 'cno'),)
#
#
# class 5142(models.Model):
#     bno = models.CharField(primary_key=True, max_length=10)
#     drug_b_count = models.IntegerField(blank=True, null=True)
#     dno = models.ForeignKey(5142, models.DO_NOTHING, db_column='dno', blank=True, null=True)
#     per_p_money = models.IntegerField(blank=True, null=True)
#     ano = models.ForeignKey(5142, models.DO_NOTHING, db_column='ano', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = '进货单5142'
#
#
# class 5142(models.Model):
#     cno = models.CharField(primary_key=True, max_length=10)
#     csex = models.CharField(max_length=1, blank=True, null=True)
#     cname = models.CharField(max_length=10, blank=True, null=True)
#     dill = models.CharField(max_length=10)
#
#     class Meta:
#         managed = False
#         db_table = '顾客5142'

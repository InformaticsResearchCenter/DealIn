# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TblCategory(models.Model):
    category = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_category'


class TblItem(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    id_store = models.ForeignKey(
        'TblStore', models.DO_NOTHING, db_column='id_store', blank=True, null=True)
    id_user = models.ForeignKey(
        'TblUser', models.DO_NOTHING, db_column='id_user', blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    images = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_item'


class TblStore(models.Model):
    store = models.CharField(max_length=50, blank=True, null=True)
    id_user = models.ForeignKey(
        'TblUser', models.DO_NOTHING, db_column='id_user', blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_store'


class TblUser(models.Model):
    username = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    birth_date = models.CharField(max_length=50, blank=True, null=True)
    role = models.IntegerField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'tbl_user'

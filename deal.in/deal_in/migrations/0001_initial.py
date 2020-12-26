# Generated by Django 3.1 on 2020-12-14 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TblCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('deleted', models.CharField(default=0, max_length=1)),
            ],
            options={
                'db_table': 'tbl_category',
            },
        ),
        migrations.CreateModel(
            name='TblDescItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('photo', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('deleted', models.CharField(default=0, max_length=1)),
            ],
            options={
                'db_table': 'tbl_desc_item',
            },
        ),
        migrations.CreateModel(
            name='TblRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=20)),
                ('deleted', models.CharField(default=0, max_length=1)),
            ],
            options={
                'db_table': 'tbl_role',
            },
        ),
        migrations.CreateModel(
            name='TblTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('status', models.IntegerField()),
                ('total', models.IntegerField()),
                ('deleted', models.CharField(default=0, max_length=1)),
            ],
            options={
                'db_table': 'tbl_transaction',
            },
        ),
        migrations.CreateModel(
            name='TblUser',
            fields=[
                ('username', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('deleted', models.CharField(default=0, max_length=1)),
                ('id_role', models.ForeignKey(db_column='id_role', on_delete=django.db.models.deletion.DO_NOTHING, to='deal_in.tblrole')),
            ],
            options={
                'db_table': 'tbl_user',
            },
        ),
        migrations.CreateModel(
            name='TblStore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store', models.CharField(blank=True, max_length=50, null=True)),
                ('deleted', models.CharField(default=0, max_length=1)),
                ('username', models.ForeignKey(blank=True, db_column='username', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='deal_in.tbluser')),
            ],
            options={
                'db_table': 'tbl_store',
            },
        ),
        migrations.CreateModel(
            name='TblItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('deleted', models.CharField(default=0, max_length=1)),
                ('id_category', models.ForeignKey(blank=True, db_column='id_category', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='deal_in.tblcategory')),
                ('id_desc', models.ForeignKey(blank=True, db_column='id_desc', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='deal_in.tbldescitem')),
                ('id_store', models.ForeignKey(blank=True, db_column='id_store', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='deal_in.tblstore')),
            ],
            options={
                'db_table': 'tbl_item',
            },
        ),
        migrations.CreateModel(
            name='TblDataTrans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.CharField(default=0, max_length=1)),
                ('id_item', models.ForeignKey(db_column='id_item', on_delete=django.db.models.deletion.DO_NOTHING, to='deal_in.tblitem')),
                ('id_trans', models.ForeignKey(db_column='id_trans', on_delete=django.db.models.deletion.DO_NOTHING, to='deal_in.tbltransaction')),
            ],
            options={
                'db_table': 'tbl_data_trans',
            },
        ),
    ]
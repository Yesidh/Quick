# Generated by Django 3.1.1 on 2020-09-05 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='code',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='bill',
            name='nit',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='client',
            name='document',
            field=models.IntegerField(),
        ),
    ]
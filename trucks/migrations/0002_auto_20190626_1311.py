# Generated by Django 2.2.1 on 2019-06-26 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trucks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trucks',
            name='description',
            field=models.CharField(default='cleared', max_length=50),
        ),
        migrations.AddField(
            model_name='trucks',
            name='exporter',
            field=models.CharField(default='cleared', max_length=50),
        ),
        migrations.AlterField(
            model_name='trucks',
            name='container',
            field=models.CharField(max_length=7),
        ),
    ]
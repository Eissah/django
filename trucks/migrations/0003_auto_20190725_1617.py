# Generated by Django 2.2.3 on 2019-07-25 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trucks', '0002_auto_20190713_1014'),
    ]

    operations = [
        migrations.CreateModel(
            name='create_invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(blank=True, null=True)),
                ('invoice_number', models.CharField(max_length=20)),
                ('month', models.CharField(blank=True, max_length=50)),
                ('amount', models.CharField(max_length=50)),
                ('created_by', models.CharField(max_length=20)),
                ('client', models.ForeignKey(on_delete='CASCADE', to='trucks.Client')),
            ],
        ),
        migrations.AlterField(
            model_name='trucks',
            name='description',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='trucks',
            name='exporter',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(blank=True, null=True)),
                ('amount_paid', models.CharField(max_length=50)),
                ('invoice_paid', models.ForeignKey(on_delete='CASCADE', to='trucks.create_invoice')),
            ],
        ),
    ]

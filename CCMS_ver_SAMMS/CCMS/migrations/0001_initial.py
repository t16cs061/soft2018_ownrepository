# Generated by Django 2.1.1 on 2019-01-09 07:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Code', models.CharField(max_length=2, validators=[django.core.validators.MinLengthValidator(1)])),
                ('CarName', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(3)])),
            ],
        ),
        migrations.CreateModel(
            name='CarReservationMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EmployeeCode', models.CharField(max_length=6, validators=[django.core.validators.MinLengthValidator(6)])),
                ('CarName', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(3)])),
                ('StartDateTime', models.DateTimeField()),
                ('EndDateTime', models.DateTimeField()),
                ('Destination', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(1)])),
                ('ETCFlag', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Code', models.CharField(max_length=6, validators=[django.core.validators.MinLengthValidator(6)])),
                ('Pass', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(6)])),
                ('Name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(3)])),
                ('Gender', models.CharField(max_length=1, validators=[django.core.validators.MinLengthValidator(1)])),
                ('Mail', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(5)])),
                ('Age', models.CharField(max_length=2, validators=[django.core.validators.MinLengthValidator(2)])),
                ('AdminFlag', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='ETCRecordMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StartDateTime', models.DateTimeField()),
                ('EndDateTime', models.DateTimeField()),
                ('CarName', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(3)])),
                ('EmployeeCode', models.CharField(max_length=6, validators=[django.core.validators.MinLengthValidator(6)])),
                ('BoardingIC', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(3)])),
                ('GetOffIC', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(3)])),
            ],
        ),
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=1000)),
                ('start_day', models.DateTimeField()),
                ('end_day', models.DateTimeField()),
                ('want_go', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MentenanceMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CarName', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(3)])),
                ('StartDateTime', models.DateTimeField()),
                ('EndDateTime', models.DateTimeField()),
                ('MentenanceOverview', models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(1)])),
            ],
        ),
        migrations.CreateModel(
            name='RefuelingRecordMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DateTime', models.DateTimeField()),
                ('SSName', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(1)])),
                ('Mileage', models.IntegerField()),
                ('Amount', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceRecordMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CarName', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(3)])),
                ('EmployeeCode', models.CharField(max_length=6, validators=[django.core.validators.MinLengthValidator(6)])),
                ('StartDateTime', models.DateTimeField()),
                ('EndDateTime', models.DateTimeField()),
                ('StartMileage', models.IntegerField()),
                ('EndMileage', models.IntegerField()),
                ('Destination', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(1)])),
                ('RefuelingFlag', models.BooleanField()),
                ('ETCFlag', models.BooleanField()),
            ],
        ),
    ]

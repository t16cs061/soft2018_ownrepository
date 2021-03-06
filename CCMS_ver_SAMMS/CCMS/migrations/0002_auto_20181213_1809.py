# Generated by Django 2.1.3 on 2018-12-13 09:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CCMS', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mail', models.EmailField(max_length=200)),
                ('age', models.IntegerField(default=0)),
                ('birthday', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='MentenanceMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CarName', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(3)])),
                ('StartDateTime', models.DateField()),
                ('EndDateTime', models.DateField()),
                ('MentenanceOverview', models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(1)])),
            ],
        ),
        migrations.RenameModel(
            old_name='employee_master',
            new_name='EmployeeMaster',
        ),
    ]

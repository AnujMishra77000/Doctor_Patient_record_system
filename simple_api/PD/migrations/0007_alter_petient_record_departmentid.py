# Generated by Django 5.1 on 2024-08-12 05:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PD', '0006_rename_department_doctors_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petient_record',
            name='DepartmentId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Petient_Record', to='PD.department'),
        ),
    ]

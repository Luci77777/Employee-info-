# Generated by Django 4.1.13 on 2024-03-29 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0008_employee_delete_receipe'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='hours_worked',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='overtime_hours',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='employee_id',
            field=models.IntegerField(null=True),
        ),
    ]
# Generated by Django 4.1.13 on 2024-03-27 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0005_alter_employees_employees_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='Employees_id',
            field=models.IntegerField(),
        ),
    ]
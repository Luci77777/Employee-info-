# Generated by Django 4.1.13 on 2024-03-27 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0003_alter_receipe_receipe_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Employees_name', models.CharField(max_length=100)),
                ('Employees_id', models.IntegerField(max_length=1000)),
            ],
        ),
        migrations.DeleteModel(
            name='Receipe',
        ),
    ]

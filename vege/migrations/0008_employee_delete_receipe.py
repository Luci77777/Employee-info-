# Generated by Django 4.1.13 on 2024-03-28 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0007_receipe_delete_employees'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=100)),
                ('employee_id', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Receipe',
        ),
    ]
# Generated by Django 4.1.13 on 2024-03-15 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_students_age_students_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='peoples',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='students',
        ),
    ]

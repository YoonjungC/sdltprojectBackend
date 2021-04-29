# Generated by Django 3.1.7 on 2021-04-29 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20210410_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_prereqs',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='course',
            name='student_experience',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='course',
            name='teachers',
            field=models.CharField(default='', max_length=200),
        ),
    ]
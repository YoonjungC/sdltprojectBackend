# Generated by Django 3.1.7 on 2021-03-19 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20210319_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_image',
            field=models.ImageField(default='images/defaultImage.jpeg', upload_to='images/'),
        ),
    ]

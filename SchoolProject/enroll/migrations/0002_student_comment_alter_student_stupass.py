# Generated by Django 4.1.3 on 2022-11-29 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='comment',
            field=models.CharField(default='not availabe ', max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='stupass',
            field=models.CharField(max_length=10),
        ),
    ]

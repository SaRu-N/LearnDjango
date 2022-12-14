# Generated by Django 4.1.3 on 2022-12-06 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Address',
            field=models.CharField(default='null', max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='Email',
            field=models.EmailField(default='null', max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='Name',
            field=models.CharField(default='null', max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='Phone',
            field=models.CharField(default='null', max_length=10),
        ),
        migrations.AlterField(
            model_name='student',
            name='Faculty',
            field=models.CharField(default='null', max_length=50),
        ),
    ]

# Generated by Django 4.1.3 on 2022-11-29 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stuid', models.IntegerField()),
                ('stuname', models.CharField(max_length=100)),
                ('stuemail', models.EmailField(max_length=254)),
                ('stupass', models.CharField(max_length=100)),
            ],
        ),
    ]
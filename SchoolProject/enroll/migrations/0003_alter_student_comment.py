# Generated by Django 4.1.3 on 2022-11-29 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0002_student_comment_alter_student_stupass'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='comment',
            field=models.CharField(default='not available', max_length=50),
        ),
    ]

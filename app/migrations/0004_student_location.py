# Generated by Django 4.2.4 on 2023-08-27 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_college_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='location',
            field=models.CharField(default='rewa', max_length=100),
        ),
    ]

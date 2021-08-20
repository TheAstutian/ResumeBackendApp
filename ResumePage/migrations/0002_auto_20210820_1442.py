# Generated by Django 3.2.6 on 2021-08-20 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ResumePage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.CharField(default='', max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(default='', max_length=30),
        ),
    ]

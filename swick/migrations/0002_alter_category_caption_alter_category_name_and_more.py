# Generated by Django 4.0.3 on 2022-04-02 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swick', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='caption',
            field=models.CharField(default='', max_length=100000),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(default='', max_length=100000),
        ),
        migrations.AlterField(
            model_name='table',
            name='name',
            field=models.CharField(default='', max_length=100000),
        ),
    ]
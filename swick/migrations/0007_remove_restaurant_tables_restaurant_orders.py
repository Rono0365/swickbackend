# Generated by Django 4.0.3 on 2022-04-04 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swick', '0006_remove_vcart_food_vcart_food'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='tables',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='orders',
            field=models.ManyToManyField(to='swick.order2'),
        ),
    ]
# Generated by Django 4.0.3 on 2022-04-02 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('swick', '0002_alter_category_caption_alter_category_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='table',
        ),
    ]
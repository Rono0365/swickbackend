# Generated by Django 4.0.3 on 2022-04-01 22:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('caption', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('price', models.CharField(default='', max_length=100)),
                ('count', models.CharField(default='1', max_length=100)),
                ('image_url', models.CharField(default='', max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu', models.ManyToManyField(to='swick.category')),
            ],
        ),
        migrations.CreateModel(
            name='order2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table', models.CharField(default='', max_length=100)),
                ('food', models.CharField(default='', max_length=10000)),
                ('restaurantx', models.CharField(default='', max_length=100)),
                ('time', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('slug', models.SlugField(null=True, unique=True)),
                ('menu', models.ManyToManyField(to='swick.menu')),
            ],
        ),
        migrations.CreateModel(
            name='restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('location', models.CharField(default='', max_length=100)),
                ('city', models.CharField(default='', max_length=100)),
                ('menu', models.ManyToManyField(to='swick.menu')),
                ('tables', models.ManyToManyField(to='swick.table')),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food', models.ManyToManyField(to='swick.food')),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swick.table')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='food',
            field=models.ManyToManyField(to='swick.food'),
        ),
    ]
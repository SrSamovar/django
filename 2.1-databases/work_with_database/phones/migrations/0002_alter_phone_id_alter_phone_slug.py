# Generated by Django 4.2.14 on 2024-09-05 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='phone',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]

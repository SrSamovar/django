# Generated by Django 4.2.14 on 2024-09-05 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0007_alter_phone_lte_exists'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]

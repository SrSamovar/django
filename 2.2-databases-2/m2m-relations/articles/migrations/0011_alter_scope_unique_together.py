# Generated by Django 4.2.14 on 2024-09-24 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0010_alter_scope_options'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='scope',
            unique_together={('article', 'is_main')},
        ),
    ]

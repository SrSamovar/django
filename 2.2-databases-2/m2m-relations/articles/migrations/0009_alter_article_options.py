# Generated by Django 4.2.14 on 2024-09-17 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_alter_article_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-published_at'], 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
    ]

# Generated by Django 3.1.7 on 2021-03-10 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_starred_info'),
    ]

    operations = [
        migrations.RenameField(
            model_name='read_info',
            old_name='read_articles',
            new_name='article',
        ),
        migrations.RenameField(
            model_name='starred_info',
            old_name='starred_articles',
            new_name='article',
        ),
    ]
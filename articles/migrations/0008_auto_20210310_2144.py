# Generated by Django 3.1.7 on 2021-03-10 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_read_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='read_info',
            name='read_articles',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.articles'),
        ),
    ]

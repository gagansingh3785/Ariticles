# Generated by Django 3.1.7 on 2021-02-26 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='image',
            field=models.ImageField(blank=True, default='images.jpg', upload_to=''),
        ),
    ]

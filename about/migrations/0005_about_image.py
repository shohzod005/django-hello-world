# Generated by Django 4.1.7 on 2023-03-10 10:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='about/%Y/%m/%d'),
            preserve_default=False,
        ),
    ]

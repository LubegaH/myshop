# Generated by Django 3.0.7 on 2020-06-08 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200608_1318'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='slug',
            field=models.SlugField(default='test-prod1'),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.0 on 2021-12-26 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='slug',
            field=models.SlugField(blank=True, max_length=127, null=True),
        ),
    ]

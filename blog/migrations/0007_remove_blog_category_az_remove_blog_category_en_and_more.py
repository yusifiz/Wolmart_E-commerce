# Generated by Django 4.0 on 2022-01-15 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_blog_category_az_blog_category_en_blog_category_ru_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='category_az',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='category_en',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='category_ru',
        ),
    ]

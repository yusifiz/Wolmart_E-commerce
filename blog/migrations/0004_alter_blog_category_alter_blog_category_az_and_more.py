# Generated by Django 4.0 on 2022-02-22 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogcategory_alter_blog_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.CharField(blank=True, max_length=127, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='category_az',
            field=models.CharField(blank=True, max_length=127, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='category_en',
            field=models.CharField(blank=True, max_length=127, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='category_ru',
            field=models.CharField(blank=True, max_length=127, null=True),
        ),
        migrations.DeleteModel(
            name='BlogCategory',
        ),
    ]
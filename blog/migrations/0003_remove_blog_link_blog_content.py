# Generated by Django 4.0 on 2021-12-25 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_options_rename_date_blog_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='link',
        ),
        migrations.AddField(
            model_name='blog',
            name='content',
            field=models.TextField(blank=True, help_text='Content', null=True),
        ),
    ]

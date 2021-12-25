# Generated by Django 4.0 on 2021-12-24 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, max_length=127, null=True)),
                ('name', models.CharField(blank=True, max_length=127, null=True)),
                ('image', models.ImageField(upload_to='blog/')),
                ('author', models.CharField(blank=True, max_length=127, null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('link', models.URLField(max_length=255)),
            ],
        ),
    ]

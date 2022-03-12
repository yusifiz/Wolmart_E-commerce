# Generated by Django 4.0 on 2022-03-12 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='home/slider/')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('desc', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
# Generated by Django 4.0 on 2022-03-02 22:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0023_shop_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adress1', models.CharField(blank=True, max_length=255, null=True)),
                ('adress2', models.CharField(blank=True, max_length=255, null=True)),
                ('town', models.CharField(blank=True, max_length=255, null=True)),
                ('zip', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('items', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.orderitem')),
            ],
        ),
    ]
# Generated by Django 4.0 on 2022-02-26 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_brand_color_shop_brand_shop_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='size',
            field=models.CharField(blank=True, choices=[('XXL', 'XXL'), ('XL', 'XL'), ('L', 'L'), ('M', 'M'), ('S', 'S'), ('XS', 'XS'), ('XXS', 'XXS')], default='M', max_length=63, null=True),
        ),
    ]
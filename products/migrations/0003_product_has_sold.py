# Generated by Django 3.2.4 on 2021-07-28 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_has_sizes'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='has_sold',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]

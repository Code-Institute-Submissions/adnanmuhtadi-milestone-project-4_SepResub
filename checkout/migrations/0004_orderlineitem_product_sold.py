# Generated by Django 3.2.4 on 2021-07-28 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_order_user_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlineitem',
            name='product_sold',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
    ]

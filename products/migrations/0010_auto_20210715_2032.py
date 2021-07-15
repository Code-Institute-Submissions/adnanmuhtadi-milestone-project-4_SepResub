# Generated by Django 3.2.4 on 2021-07-15 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20210715_2029'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='imagetwo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='product',
            name='imagetwo_url',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
    ]

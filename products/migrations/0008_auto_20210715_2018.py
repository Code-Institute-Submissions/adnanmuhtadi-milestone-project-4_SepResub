# Generated by Django 3.2.4 on 2021-07-15 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20210715_2001'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='image1',
            new_name='image_four',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='image2',
            new_name='image_one',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='image3',
            new_name='image_three',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='image4',
            new_name='image_two',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='image_url1',
            new_name='image_url_four',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='image_url2',
            new_name='image_url_one',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='image_url3',
            new_name='image_url_three',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='image_url4',
            new_name='image_url_two',
        ),
    ]

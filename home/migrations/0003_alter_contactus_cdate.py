# Generated by Django 3.2.4 on 2021-07-27 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210727_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='cdate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
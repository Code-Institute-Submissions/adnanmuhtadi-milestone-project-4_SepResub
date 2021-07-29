# Generated by Django 3.2.4 on 2021-07-28 13:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0005_rename_user_contactus_cuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='cuser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
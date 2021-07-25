# Generated by Django 3.2.4 on 2021-07-24 23:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_date', models.DateTimeField(auto_now_add=True)),
                ('user_test_title', models.CharField(max_length=254)),
                ('user_message', models.TextField()),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('user_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='profiles.userprofile')),
            ],
        ),
    ]

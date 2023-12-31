# Generated by Django 4.2.7 on 2023-12-30 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dj_socialapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_info',
            name='full_name',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='user_info',
            name='user_banner',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user_info',
            name='user_profileimage',
            field=models.CharField(max_length=200, null=True),
        ),
    ]

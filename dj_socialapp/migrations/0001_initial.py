# Generated by Django 4.2.7 on 2023-12-29 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.CharField(max_length=150, null=True)),
                ('user_name', models.CharField(max_length=100)),
                ('user_id', models.IntegerField(null=True)),
            ],
        ),
    ]

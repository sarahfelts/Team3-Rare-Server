# Generated by Django 4.2.13 on 2024-06-20 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rareapi', '0003_rareuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rareuser',
            name='username',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]

# Generated by Django 4.2.13 on 2024-07-23 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rareapi', '0004_alter_rareuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='approved',
            field=models.BooleanField(),
        ),
    ]
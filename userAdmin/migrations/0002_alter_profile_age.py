# Generated by Django 5.0.2 on 2024-08-24 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userAdmin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.IntegerField(),
        ),
    ]

# Generated by Django 5.0.2 on 2024-03-10 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0004_alter_sizecloth_size_cloth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sizecloth',
            name='size_cloth',
            field=models.IntegerField(),
        ),
    ]

# Generated by Django 2.1 on 2018-10-18 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_auto_20181017_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='date',
            field=models.DateField(),
        ),
    ]

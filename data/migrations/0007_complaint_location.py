# Generated by Django 2.1 on 2018-11-21 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0006_auto_20181105_0302'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='location',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]

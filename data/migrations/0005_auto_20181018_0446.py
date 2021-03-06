# Generated by Django 2.1 on 2018-10-18 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_auto_20181018_0235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='district',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='file_no',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='officer',
            name='first_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='officer',
            name='last_name',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='officer',
            name='rank',
            field=models.CharField(max_length=200),
        ),
    ]

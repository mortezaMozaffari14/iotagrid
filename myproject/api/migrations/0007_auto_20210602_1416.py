# Generated by Django 3.0.8 on 2021-06-02 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20210602_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='output',
            field=models.CharField(max_length=200, null=True),
        ),
    ]

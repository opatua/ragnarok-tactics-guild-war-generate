# Generated by Django 2.2.13 on 2020-08-25 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ragnarok', '0012_auto_20200626_2308'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='real_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='historicalcharacter',
            name='real_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

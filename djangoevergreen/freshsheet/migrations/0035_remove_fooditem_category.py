# Generated by Django 2.0.1 on 2018-01-10 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('freshsheet', '0034_auto_20180110_0007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fooditem',
            name='category',
        ),
    ]
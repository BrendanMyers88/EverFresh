# Generated by Django 2.0.1 on 2018-01-05 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freshsheet', '0013_auto_20180104_2210'),
    ]

    operations = [
        migrations.AddField(
            model_name='farm',
            name='color',
            field=models.CharField(default='', max_length=20),
        ),
    ]
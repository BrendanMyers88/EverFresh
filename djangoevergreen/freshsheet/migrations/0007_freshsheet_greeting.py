# Generated by Django 2.0.1 on 2018-05-09 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freshsheet', '0006_order_order_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='freshsheet',
            name='greeting',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]

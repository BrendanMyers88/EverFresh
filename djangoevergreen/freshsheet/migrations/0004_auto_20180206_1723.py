# Generated by Django 2.0.1 on 2018-02-06 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freshsheet', '0003_auto_20180206_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('S', 'Pending'), ('C', 'Complete'), ('O', 'Out For Delivery'), ('D', 'Delivered')], default='Shopping', max_length=40),
        ),
    ]

# Generated by Django 2.0.1 on 2018-02-08 23:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('freshsheet', '0004_auto_20180206_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='unit',
            field=models.CharField(choices=[('LB', 'Pound(s)'), ('BU', 'Bundle'), ('HD', 'Head'), ('C', 'Count')], default=('LB', 'Pound(s)'), max_length=15),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('P', 'Pending'), ('C', 'Complete'), ('O', 'Out For Delivery'), ('D', 'Delivered')], default='Shopping', max_length=40),
        ),
    ]
# Generated by Django 2.0.1 on 2018-11-16 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freshsheet', '0027_auto_20181115_0139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountrequest',
            name='message_box',
            field=models.TextField(default='', max_length=2000, verbose_name='Message'),
        ),
    ]
# Generated by Django 2.0.1 on 2018-10-10 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freshsheet', '0024_remove_user_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='fooditem',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 2.0.1 on 2018-07-20 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freshsheet', '0021_auto_20180706_2014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='farm',
            name='ribbon_color',
        ),
        migrations.AlterField(
            model_name='farm',
            name='city',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='farm',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='farm',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='farm',
            name='state',
            field=models.CharField(blank=True, choices=[('AL', 'Alabama'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')], default='WA', max_length=40, null=True),
        ),
    ]

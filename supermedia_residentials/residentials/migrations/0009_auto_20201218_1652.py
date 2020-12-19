# Generated by Django 3.1.4 on 2020-12-18 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('residentials', '0008_auto_20201218_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buildings',
            name='KI_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='buildings',
            name='internal_net_property',
            field=models.IntegerField(choices=[(1, 'SM'), (2, 'SM/JMDI'), (3, 'SM/UPC'), (4, 'SM/UPC/ Vectra'), (5, 'SM/Wspólnota'), (6, 'Wspólnota'), (7, 'bd')], default=7),
        ),
        migrations.AlterField(
            model_name='persons',
            name='phone',
            field=models.IntegerField(default=0),
        ),
    ]

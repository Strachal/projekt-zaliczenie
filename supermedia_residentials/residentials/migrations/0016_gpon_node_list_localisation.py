# Generated by Django 3.1.4 on 2020-12-28 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('residentials', '0015_auto_20201221_0949'),
    ]

    operations = [
        migrations.AddField(
            model_name='gpon_node_list',
            name='localisation',
            field=models.CharField(default='', max_length=64),
        ),
    ]

# Generated by Django 3.1.4 on 2020-12-11 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rg6_50_percent', models.CharField(max_length=15)),
                ('rg6_30_percent', models.CharField(max_length=15)),
                ('rg6_33_percent', models.CharField(max_length=15)),
                ('backbone_ftth', models.CharField(max_length=15)),
                ('backbone_lan', models.CharField(max_length=15)),
                ('backbone_catv', models.CharField(max_length=15)),
                ('connection', models.CharField(max_length=15)),
                ('ftth_100_percent', models.CharField(max_length=15)),
                ('utp_100_percent', models.CharField(max_length=15)),
                ('rg6_100_percent', models.CharField(max_length=15)),
                ('sewerage', models.CharField(max_length=15)),
                ('money_to_deweloper', models.CharField(max_length=15)),
                ('ftth_reserves', models.CharField(max_length=15)),
                ('mast_radio', models.CharField(max_length=15)),
                ('utp_reserves_50_percent', models.CharField(max_length=15)),
                ('rg6_zit_100_percent', models.CharField(max_length=15)),
                ('zit', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='AllDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_Launch_services', models.DateField()),
                ('year_Launch_services', models.DateField()),
                ('month_Launch_services', models.DateField()),
                ('quarter_Launch_services', models.IntegerField(choices=[(1, 'I kw.'), (2, 'II kw.'), (3, 'III kw.'), (4, 'IV kw.')])),
                ('date_card_project', models.DateField()),
                ('date_agreement', models.DateField()),
                ('date_estimated_budget_order', models.DateField()),
                ('date_estimated_budget_execution', models.DateField()),
                ('date_estimated_budget_to_fill', models.DateField()),
                ('date_estimated_budget_accept', models.DateField()),
                ('date_internal_net_order', models.DateField()),
                ('date_internal_net_execution', models.DateField()),
                ('date_FO_question_of_price', models.DateField()),
                ('date_FO_answer_with_price', models.DateField()),
                ('date_FO_order', models.DateField()),
                ('date_FO_execution', models.DateField()),
                ('date_LAN_GPON_launch', models.DateField()),
                ('date_CATV_IPTV_launch', models.DateField()),
                ('date_reckoning', models.DateField()),
                ('date_expenditure_FO', models.DateField()),
                ('date_expenditure_avtive_elements', models.DateField()),
                ('date_expenditure_inactive_elements', models.DateField()),
                ('date_expenditure_sewerage', models.DateField()),
                ('date_expenditure_OLT', models.DateField()),
                ('date_expenditure_for_deweloper', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Competitors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Opl', models.CharField(max_length=15)),
                ('Upc', models.CharField(max_length=15)),
                ('Vectra', models.CharField(max_length=15)),
                ('Jmdi', models.CharField(max_length=15)),
                ('MetroInternet', models.CharField(max_length=15)),
                ('Netia', models.CharField(max_length=15)),
                ('Other', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Finances',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_total', models.FloatField()),
                ('amount_FO', models.FloatField()),
                ('amount_sewerage', models.FloatField()),
                ('amount_internal_network', models.FloatField()),
                ('amount_to_reckoning_budget', models.FloatField()),
                ('amount_CN_to_reckoning_budget', models.FloatField()),
                ('amount_sewerage_to_reckoning_budget', models.FloatField()),
                ('amount_per_HP_without_FO', models.FloatField()),
                ('amount_per_HP_with_FO', models.FloatField()),
                ('amount_inactive_elements', models.FloatField()),
                ('amount_active_elements', models.FloatField()),
                ('amount_activity', models.FloatField()),
                ('amount_OLT', models.FloatField()),
                ('amount_for_deweloper', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='General',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='GPON_node_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_RT', models.URLField()),
                ('link_RT_FO', models.URLField()),
                ('link_KI', models.URLField()),
                ('link_SMP_osiedle', models.URLField()),
                ('link_SMP_FO', models.URLField()),
                ('link_kosztorys_ryczałtowy', models.URLField()),
                ('link_kosztorys_rozliczony', models.URLField()),
                ('link_skan_umowy', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Raport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Persons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_last_name', models.CharField(max_length=40)),
                ('job', models.CharField(max_length=20)),
                ('phone', models.IntegerField()),
                ('email', models.CharField(max_length=64)),
                ('SM_PM_initial', models.CharField(max_length=4)),
                ('deweloper_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='residentials.developer')),
                ('general_contractor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='residentials.general')),
            ],
        ),
        migrations.CreateModel(
            name='Buildings',
            fields=[
                ('PK_number', models.AutoField(primary_key=True, serialize=False)),
                ('KI_number', models.IntegerField()),
                ('MPK_number', models.CharField(max_length=10)),
                ('MPK_number_sewerage', models.CharField(max_length=10)),
                ('building_name', models.CharField(max_length=255)),
                ('building_adres', models.CharField(max_length=255)),
                ('parcel_number', models.CharField(max_length=255)),
                ('quantity_HP', models.IntegerField()),
                ('quantity_LU', models.IntegerField()),
                ('estimated_budget_accept', models.IntegerField(choices=[(1, 'yes'), (2, 'no'), (2, 'in progress')])),
                ('flat_price', models.FloatField()),
                ('kind_of_inhabitation', models.IntegerField(choices=[(1, 'zasiedlone'), (2, 'w trakcie'), (3, 'deweloper')])),
                ('status', models.IntegerField(choices=[(1, 'realizacja'), (2, 'eksploatacja'), (3, 'niezrealizowane'), (4, 'negocjacje'), (5, 'chcemy'), (6, 'inwestycja wstrzymana')])),
                ('services_provided', models.IntegerField(choices=[(1, 'GPON/IPTV'), (2, 'GPON/CATV'), (3, 'LAN/CATV'), (4, 'LAN')])),
                ('internal_net_property', models.IntegerField(choices=[(1, 'SM'), (2, 'SM/JMDI'), (3, 'SM/UPC'), (4, 'SM/UPC/ Vectra'), (5, 'SM/Wspólnota'), (6, 'Wspólnota')])),
                ('remarks_of_MS', models.TextField()),
                ('remarks_of_AK', models.TextField()),
                ('GPON_node_localisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='residentials.gpon_node_list')),
                ('competitors', models.ManyToManyField(to='residentials.Competitors')),
                ('range_of_activity', models.ManyToManyField(to='residentials.Activities')),
            ],
        ),
    ]

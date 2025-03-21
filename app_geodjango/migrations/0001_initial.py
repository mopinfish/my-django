# Generated by Django 5.1.3 on 2025-01-03 07:19

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='city_border',
            fields=[
                ('key_code', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('city_name', models.CharField(max_length=24, null=True)),
                ('geom', django.contrib.gis.db.models.fields.PolygonField(srid=6677)),
            ],
        ),
        migrations.CreateModel(
            name='stations',
            fields=[
                ('station_cd', models.CharField(max_length=254, primary_key=True, serialize=False)),
                ('station_g_field', models.CharField(max_length=254)),
                ('station_na', models.CharField(max_length=254)),
                ('station_1', models.CharField(max_length=254, null=True)),
                ('station_2', models.CharField(max_length=254, null=True)),
                ('line_cd', models.CharField(max_length=254)),
                ('pref_cd', models.CharField(max_length=254)),
                ('post', models.CharField(max_length=254)),
                ('address', models.CharField(max_length=254)),
                ('lon', models.FloatField()),
                ('lat', models.FloatField()),
                ('open_ymd', models.CharField(max_length=254)),
                ('close_ymd', models.CharField(max_length=254)),
                ('e_status', models.CharField(max_length=254)),
                ('e_sort', models.CharField(max_length=254)),
                ('station_3', models.CharField(max_length=254, null=True)),
                ('circuity_a', models.CharField(max_length=254, null=True)),
                ('edge_densi', models.CharField(max_length=254, null=True)),
                ('edge_lengt', models.CharField(max_length=254, null=True)),
                ('edge_len_1', models.CharField(max_length=254, null=True)),
                ('intersecti', models.CharField(max_length=254, null=True)),
                ('intersec_1', models.CharField(max_length=254, null=True)),
                ('k_avg', models.CharField(max_length=254, null=True)),
                ('m', models.CharField(max_length=254, null=True)),
                ('n', models.CharField(max_length=254, null=True)),
                ('node_densi', models.CharField(max_length=254, null=True)),
                ('self_loop_field', models.CharField(max_length=254, null=True)),
                ('street_den', models.CharField(max_length=254, null=True)),
                ('street_len', models.CharField(max_length=254, null=True)),
                ('street_l_1', models.CharField(max_length=254, null=True)),
                ('street_seg', models.CharField(max_length=254, null=True)),
                ('streets_pe', models.CharField(max_length=254, null=True)),
                ('average_cl', models.CharField(max_length=254, null=True)),
                ('mean_integ', models.CharField(max_length=254, null=True)),
                ('num_commun', models.CharField(max_length=254, null=True)),
                ('modularity', models.CharField(max_length=254, null=True)),
                ('var_integr', models.CharField(max_length=254, null=True)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
    ]

# Generated by Django 5.1.4 on 2025-03-03 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('open3d_map', '0007_alter_movie_cultural_property'),
    ]

    operations = [
        migrations.AlterField(
            model_name='culturalproperty',
            name='category',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]

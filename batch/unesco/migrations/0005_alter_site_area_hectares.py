# Generated by Django 4.0.7 on 2023-02-06 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unesco', '0004_alter_site_area_hectares'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='area_hectares',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]

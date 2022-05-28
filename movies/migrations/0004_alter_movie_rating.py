# Generated by Django 4.0.4 on 2022-05-28 18:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_remove_movie_daily_rate_remove_movie_number_in_stock_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.FloatField(null=True, validators=[django.core.validators.MaxValueValidator(10.0)]),
        ),
    ]
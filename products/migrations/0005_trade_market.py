# Generated by Django 5.0.1 on 2024-03-27 10:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
        ('products', '0004_alter_products_bar_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='trade',
            name='market',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='trade', to='market.market'),
        ),
    ]
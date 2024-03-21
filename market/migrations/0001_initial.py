# Generated by Django 5.0.3 on 2024-03-21 11:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('stir', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('today_debt', models.DecimalField(decimal_places=2, max_digits=10)),
                ('debt_collection', models.DecimalField(decimal_places=2, max_digits=10)),
                ('debts', models.DecimalField(decimal_places=2, max_digits=10)),
                ('today_trade', models.DecimalField(decimal_places=2, max_digits=10)),
                ('trade', models.DecimalField(decimal_places=2, max_digits=10)),
                ('market', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='statistics', to='market.market')),
            ],
        ),
    ]

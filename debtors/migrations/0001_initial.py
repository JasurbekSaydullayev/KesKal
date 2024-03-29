# Generated by Django 5.0.3 on 2024-03-21 11:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('market', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Debtor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=13, unique=True)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('comment', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('paid', models.BooleanField(default=False)),
                ('market', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='debtors', to='market.market')),
                ('products', models.ManyToManyField(related_name='debtors', to='products.products')),
            ],
        ),
    ]

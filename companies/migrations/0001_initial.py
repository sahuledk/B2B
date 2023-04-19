# Generated by Django 4.1.5 on 2023-01-22 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Balance_amount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance_amount', models.IntegerField()),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.currencies')),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=1000)),
                ('pdf_type', models.CharField(max_length=1000)),
                ('order_validity_month', models.IntegerField()),
                ('balance_amount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.balance_amount')),
            ],
        ),
    ]
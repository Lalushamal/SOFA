# Generated by Django 5.0 on 2024-03-12 10:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cart", "0004_alter_orderproduct_order"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orderproduct",
            name="order",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="cart.order"
            ),
        ),
    ]

# Generated by Django 5.1.7 on 2025-03-17 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_order_total_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='book_price',
        ),
        migrations.RemoveField(
            model_name='order',
            name='book_quantity',
        ),
        migrations.RemoveField(
            model_name='order',
            name='book_title',
        ),
        migrations.AddField(
            model_name='order',
            name='cart',
            field=models.JSONField(default='default_cart_value'),
            preserve_default=False,
        ),
    ]

# Generated by Django 5.1.7 on 2025-03-20 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_alter_order_total_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('total_value', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]

# Generated by Django 5.1.1 on 2024-09-19 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_order_products_delete_product'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]

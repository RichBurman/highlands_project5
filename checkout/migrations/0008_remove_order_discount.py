# Generated by Django 3.2.23 on 2023-11-14 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0007_order_discount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='discount',
        ),
    ]

# Generated by Django 3.2.23 on 2023-11-14 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0010_discountcode_used'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discountcode',
            name='used',
        ),
    ]

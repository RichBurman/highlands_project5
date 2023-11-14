# Generated by Django 3.2.23 on 2023-11-14 09:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0003_alter_cart_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DiscountCode',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='discount_code',
        ),
        migrations.AlterField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

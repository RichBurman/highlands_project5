# Generated by Django 3.2.23 on 2023-11-15 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0003_auto_20231115_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='difficulty_rating',
            field=models.CharField(choices=[('Easy', 'Easy'), ('Moderate', 'Moderate'), ('difficult', 'Difficult'), ('Challenging', 'Challenging')], default='Easy', max_length=20),
        ),
    ]
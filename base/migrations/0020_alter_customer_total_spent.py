# Generated by Django 4.1.7 on 2023-05-06 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_customer_total_spent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='total_spent',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]

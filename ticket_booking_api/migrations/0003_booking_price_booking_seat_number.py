# Generated by Django 4.2.2 on 2023-06-12 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_booking_api', '0002_alter_booking_customer_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='seat_number',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]

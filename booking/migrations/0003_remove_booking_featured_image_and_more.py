# Generated by Django 4.2.21 on 2025-05-22 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_booking_featured_image_customer_featured_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='featured_image',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='featured_image',
        ),
        migrations.AddField(
            model_name='booking',
            name='email',
            field=models.EmailField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='booking',
            name='full_name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='booking',
            name='phone_number',
            field=models.CharField(default='0000000000', max_length=20),
        ),
    ]

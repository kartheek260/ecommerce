# Generated by Django 2.2.6 on 2019-11-13 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartapp', '0003_cart_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]

# Generated by Django 2.2.6 on 2019-11-05 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='username',
            field=models.EmailField(max_length=20),
        ),
    ]

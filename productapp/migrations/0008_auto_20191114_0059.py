# Generated by Django 2.2.6 on 2019-11-13 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0007_auto_20191113_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pimage',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
    ]

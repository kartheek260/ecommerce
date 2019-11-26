# Generated by Django 2.2.6 on 2019-10-31 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='stock',
            fields=[
                ('prodid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='productapp.product')),
                ('tot_qty', models.IntegerField()),
                ('last_update', models.DateField()),
                ('next_update', models.DateField()),
            ],
        ),
    ]

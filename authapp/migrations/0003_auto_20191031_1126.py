# Generated by Django 2.2.6 on 2019-10-31 05:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_auto_20191021_1245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registers',
            name='Gender',
        ),
        migrations.RemoveField(
            model_name='registers',
            name='area_code',
        ),
    ]

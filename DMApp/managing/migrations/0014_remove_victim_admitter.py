# Generated by Django 2.0.5 on 2018-10-24 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('managing', '0013_auto_20181024_1951'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='victim',
            name='admitter',
        ),
    ]

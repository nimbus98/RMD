# Generated by Django 2.0.5 on 2018-10-24 14:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('managing', '0003_auto_20181024_1919'),
    ]

    operations = [
        migrations.RenameField(
            model_name='victim',
            old_name='thumb',
            new_name='victim_photo',
        ),
        migrations.AddField(
            model_name='victim',
            name='hospital_address',
            field=models.TextField(default='Add Hospital/Relief Camp Address'),
        ),
        migrations.AlterField(
            model_name='victim',
            name='admitter',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
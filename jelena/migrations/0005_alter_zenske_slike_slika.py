# Generated by Django 5.0.11 on 2025-01-27 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jelena', '0004_alter_zenske_slike_options_zenske_slike_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zenske_slike',
            name='slika',
            field=models.ImageField(blank=True, null=True, upload_to='frizure'),
        ),
    ]

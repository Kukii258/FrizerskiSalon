# Generated by Django 5.0.11 on 2025-01-27 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jelena', '0003_zenske_slike'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='zenske_slike',
            options={'verbose_name_plural': 'Zenske Slike'},
        ),
        migrations.AddField(
            model_name='zenske_slike',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='frizure/frizure_video'),
        ),
    ]

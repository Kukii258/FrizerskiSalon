# Generated by Django 5.0.11 on 2025-01-30 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jelena', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Djecje_frizure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ime', models.CharField(max_length=100)),
                ('cijena', models.IntegerField()),
                ('opis', models.CharField(blank=True)),
                ('slika', models.ImageField(blank=True, null=True, upload_to='frizure')),
                ('video', models.FileField(blank=True, null=True, upload_to='frizure_video')),
                ('pocetna_stranica', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Djecje Frizure',
            },
        ),
        migrations.CreateModel(
            name='Muske_frizure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ime', models.CharField(max_length=100)),
                ('cijena', models.IntegerField()),
                ('opis', models.CharField(blank=True)),
                ('slika', models.ImageField(blank=True, null=True, upload_to='frizure')),
                ('video', models.FileField(blank=True, null=True, upload_to='frizure_video')),
                ('pocetna_stranica', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Muske Frizure',
            },
        ),
        migrations.CreateModel(
            name='Produkti',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ime', models.CharField(max_length=100)),
                ('cijena', models.IntegerField()),
                ('opis', models.CharField(blank=True)),
                ('slika', models.ImageField(blank=True, null=True, upload_to='frizure')),
                ('video', models.FileField(blank=True, null=True, upload_to='frizure_video')),
                ('pocetna_stranica', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Produkti',
            },
        ),
        migrations.CreateModel(
            name='Zenske_frizure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ime', models.CharField(max_length=100)),
                ('cijena', models.IntegerField()),
                ('opis', models.CharField(blank=True)),
                ('slika', models.ImageField(blank=True, null=True, upload_to='frizure')),
                ('video', models.FileField(blank=True, null=True, upload_to='frizure_video')),
                ('pocetna_stranica', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Zenske Frizure',
            },
        ),
        migrations.AlterModelOptions(
            name='obavijest',
            options={'verbose_name_plural': 'Obavijesti'},
        ),
        migrations.AlterField(
            model_name='obavijest',
            name='pod_naslov',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='obavijest',
            name='slika',
            field=models.ImageField(blank=True, upload_to='obavijest_slike'),
        ),
    ]

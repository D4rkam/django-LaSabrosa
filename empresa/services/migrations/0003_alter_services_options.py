# Generated by Django 4.0.1 on 2022-01-25 04:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_alter_services_options_services_published'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='services',
            options={'ordering': ['-created'], 'verbose_name': 'Servicios', 'verbose_name_plural': 'Servicios'},
        ),
    ]
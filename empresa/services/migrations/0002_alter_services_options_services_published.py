# Generated by Django 4.0.1 on 2022-01-23 22:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='services',
            options={'ordering': ('-created',), 'verbose_name': 'Servicios', 'verbose_name_plural': 'Servicios'},
        ),
        migrations.AddField(
            model_name='services',
            name='published',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de Publicación'),
        ),
    ]
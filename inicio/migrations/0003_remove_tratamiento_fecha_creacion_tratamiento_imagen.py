# Generated by Django 4.2.7 on 2023-11-14 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0002_sobremi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tratamiento',
            name='fecha_creacion',
        ),
        migrations.AddField(
            model_name='tratamiento',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='tratamientos/'),
        ),
    ]
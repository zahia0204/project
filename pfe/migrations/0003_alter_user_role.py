# Generated by Django 5.1.7 on 2025-03-23 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pfe', '0002_alter_client_region_delete_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[(1, 'Admin'), (2, 'Responsable de Boufarik'), (3, 'Responsable de Mouzaia'), (4, 'Responsable de Larbaa'), (5, 'Responsable de Oulad Yaich'), (6, 'Responsable de El Wouroud'), (7, 'Responsable de Bougara'), (8, 'Responsable de Afroun')], max_length=30),
        ),
    ]

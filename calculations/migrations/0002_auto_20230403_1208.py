# Generated by Django 2.2 on 2023-04-03 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculations', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deliveries',
            old_name='non_stricker',
            new_name='non_striker',
        ),
    ]

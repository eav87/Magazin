# Generated by Django 4.1.7 on 2023-03-29 02:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pervi_sait', '0002_rename_bd_auto_auto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auto',
            old_name='auto_3',
            new_name='data',
        ),
        migrations.RenameField(
            model_name='auto',
            old_name='auto_2',
            new_name='harakteristika',
        ),
        migrations.RenameField(
            model_name='auto',
            old_name='auto',
            new_name='marka',
        ),
        migrations.RenameField(
            model_name='auto',
            old_name='auto_1',
            new_name='model',
        ),
    ]

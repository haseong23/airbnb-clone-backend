# Generated by Django 5.1.1 on 2024-09-20 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='laguage',
            new_name='language',
        ),
    ]

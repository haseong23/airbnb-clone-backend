# Generated by Django 5.1.1 on 2024-09-20 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('price_per_night', models.PositiveBigIntegerField()),
                ('discription', models.TextField()),
                ('address', models.CharField(max_length=1500)),
                ('pets_allowed', models.BooleanField(default=False)),
            ],
        ),
    ]

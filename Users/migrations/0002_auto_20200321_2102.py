# Generated by Django 3.0.4 on 2020-03-21 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='phone',
            field=models.CharField(max_length=11),
        ),
    ]

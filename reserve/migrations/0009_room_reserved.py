# Generated by Django 3.0.1 on 2020-09-03 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0008_auto_20200816_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='reserved',
            field=models.BooleanField(default=False),
        ),
    ]

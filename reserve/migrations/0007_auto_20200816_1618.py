# Generated by Django 3.0.1 on 2020-08-16 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0006_auto_20200816_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reserve.Location'),
        ),
    ]
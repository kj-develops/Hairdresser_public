# Generated by Django 4.0.1 on 2022-05-09 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('betakroll', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='nameHairdresser',
        ),
        migrations.AddField(
            model_name='booking',
            name='hairdresser',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
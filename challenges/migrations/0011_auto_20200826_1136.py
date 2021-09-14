# Generated by Django 3.1 on 2020-08-26 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0010_delete_achievement'),
    ]

    operations = [
        migrations.AddField(
            model_name='mountain',
            name='duration',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='mountain',
            name='distance',
            field=models.FloatField(default=0),
        ),
    ]
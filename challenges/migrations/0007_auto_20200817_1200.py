# Generated by Django 3.1 on 2020-08-17 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0006_auto_20200817_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achivement',
            name='challenge_completed',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='challenges.challenge'),
        ),
        migrations.AlterField(
            model_name='achivement',
            name='mountain_completed',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='challenges.mountain'),
        ),
    ]

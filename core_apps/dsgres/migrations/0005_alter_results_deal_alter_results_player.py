# Generated by Django 4.1.4 on 2023-02-04 23:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("dsgres", "0004_results_player"),
    ]

    operations = [
        migrations.AlterField(
            model_name="results",
            name="deal",
            field=models.DecimalField(
                decimal_places=3,
                default=0.0,
                max_digits=10,
                verbose_name="Affiliate Deal",
            ),
        ),
        migrations.AlterField(
            model_name="results",
            name="player",
            field=models.ForeignKey(
                default=2,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="nickname3",
                to=settings.AUTH_USER_MODEL,
                verbose_name="user",
            ),
        ),
    ]

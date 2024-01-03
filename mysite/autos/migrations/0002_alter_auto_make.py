# Generated by Django 4.2.7 on 2023-12-30 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("autos", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="auto",
            name="make",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="autos",
                to="autos.make",
            ),
        ),
    ]

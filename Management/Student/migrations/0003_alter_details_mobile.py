# Generated by Django 5.0.1 on 2024-01-10 06:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Student", "0002_details_course"),
    ]

    operations = [
        migrations.AlterField(
            model_name="details",
            name="mobile",
            field=models.CharField(max_length=255),
        ),
    ]
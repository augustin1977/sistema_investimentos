# Generated by Django 4.2.16 on 2024-10-22 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Investimentos", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="investimento",
            name="data",
            field=models.DateField(),
        ),
    ]

# Generated by Django 5.1.1 on 2024-09-13 09:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("gallerydept", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="materials",
            field=models.CharField(
                default=None, max_length=70, verbose_name="Матерьялы"
            ),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.1.1 on 2022-11-01 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("e_portal", "0014_merge_20221101_2113"),
    ]

    operations = [
        migrations.AddField(
            model_name="customers",
            name="avatar",
            field=models.ImageField(blank=True, upload_to="resources/img/avatars"),
        ),
        migrations.AddField(
            model_name="operators",
            name="avatar",
            field=models.ImageField(blank=True, upload_to="resources/img/avatars"),
        ),
    ]

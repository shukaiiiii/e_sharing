# Generated by Django 4.1.1 on 2022-10-31 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("e_portal", "0012_alter_vehicles_description_alter_vehicles_locname"),
    ]

    operations = [
        migrations.RenameModel(old_name="Manangers", new_name="Managers",),
        migrations.AlterField(
            model_name="vehicles",
            name="cover",
            field=models.ImageField(blank=True, upload_to="resources/img/covers"),
        ),
        migrations.AlterField(
            model_name="vehicles",
            name="status",
            field=models.CharField(default="available", max_length=32),
        ),
    ]

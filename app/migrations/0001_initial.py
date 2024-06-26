# Generated by Django 4.2.5 on 2023-10-31 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Movie",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(upload_to="images/")),
                ("name", models.CharField(max_length=50)),
                ("time", models.CharField(max_length=20)),
                ("release", models.DateField()),
                ("vedioadjactive", models.CharField(max_length=10)),
                ("syujeti", models.CharField(max_length=50)),
                ("genre", models.CharField(max_length=50)),
                ("director", models.CharField(max_length=50)),
                ("title", models.TextField()),
                ("country", models.CharField(max_length=40)),
                ("vedio", models.FileField(upload_to="film/")),
                ("baholash", models.IntegerField()),
            ],
        ),
    ]

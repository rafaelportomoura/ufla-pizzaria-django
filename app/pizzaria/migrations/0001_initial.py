# Generated by Django 4.2.1 on 2023-06-06 00:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import pizzaria.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "name",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Client",
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
                ("first_name", models.CharField(max_length=20)),
                ("last_name", models.CharField(max_length=80)),
                ("created_at", models.TimeField(auto_now_add=True)),
                ("phone", models.CharField(max_length=20)),
                (
                    "status",
                    models.IntegerField(choices=[(0, "INACTIVE"), (1, "ACTIVE")]),
                ),
                (
                    "user_id",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=30, unique=True)),
                ("description", models.CharField(max_length=45)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "picture",
                    models.ImageField(upload_to=pizzaria.models.product_file_path),
                ),
                (
                    "status",
                    models.IntegerField(
                        choices=[(0, "Lacking"), (1, "Available")], default=1
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="pizzaria.category",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Order",
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
                (
                    "status",
                    models.IntegerField(
                        choices=[
                            (0, "Cancelled"),
                            (1, "Placed"),
                            (2, "Processing"),
                            (3, "Completed"),
                        ],
                        default=1,
                    ),
                ),
                ("datetime", models.DateField(auto_now_add=True)),
                (
                    "client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="pizzaria.client",
                    ),
                ),
                (
                    "employee",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.RESTRICT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("products", models.ManyToManyField(to="pizzaria.product")),
            ],
        ),
        migrations.CreateModel(
            name="Cart",
            fields=[
                (
                    "client",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="pizzaria.client",
                    ),
                ),
                ("products", models.ManyToManyField(to="pizzaria.product")),
            ],
        ),
    ]
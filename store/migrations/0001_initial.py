# Generated by Django 3.2.7 on 2021-09-12 17:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import store.models


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
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(db_index=True, max_length=255)),
                ("slug", models.SlugField(unique=True)),
            ],
            options={
                "verbose_name_plural": "Categories",
            },
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
                ("title", models.CharField(max_length=255)),
                ("slug", models.SlugField(unique=True)),
                ("author", models.CharField(default="admin", max_length=255)),
                ("description", models.TextField(blank=True)),
                ("image", models.ImageField(upload_to=store.models.product_image)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("in_stock", models.BooleanField(default=True)),
                ("is_active", models.BooleanField(default=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="products",
                        to="store.category",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="product_creator",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Products",
                "ordering": ("-created",),
            },
        ),
    ]
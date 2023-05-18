# Generated by Django 4.1.3 on 2022-12-15 09:03

import django.db.models.deletion
import versatileimagefield.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AdminNumber",
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
                ("name", models.CharField(blank=True, max_length=20, null=True)),
                (
                    "phone_number",
                    models.CharField(blank=True, max_length=12, null=True),
                ),
            ],
        ),
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
                (
                    "category",
                    models.CharField(
                        blank=True, max_length=200, null=True, unique=True
                    ),
                ),
                (
                    "image",
                    versatileimagefield.fields.VersatileImageField(
                        blank=True, null=True, upload_to="categories/"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="HeaderFlash",
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
                ("address", models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Login",
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
                    "customer_name",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("password", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "phone_number",
                    models.CharField(blank=True, max_length=10, null=True, unique=True),
                ),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                ("address", models.CharField(blank=True, max_length=250, null=True)),
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
                ("product", models.CharField(max_length=150)),
                (
                    "image",
                    versatileimagefield.fields.VersatileImageField(
                        blank=True, null=True, upload_to="products/"
                    ),
                ),
                (
                    "sub_image1",
                    versatileimagefield.fields.VersatileImageField(
                        blank=True, null=True, upload_to="products/"
                    ),
                ),
                (
                    "sub_image2",
                    versatileimagefield.fields.VersatileImageField(
                        blank=True, null=True, upload_to="products/"
                    ),
                ),
                (
                    "sub_image3",
                    versatileimagefield.fields.VersatileImageField(
                        blank=True, null=True, upload_to="products/"
                    ),
                ),
                ("price", models.IntegerField(blank=True, null=True)),
                ("offer_price", models.IntegerField(blank=True, null=True)),
                (
                    "rentalsecurity",
                    models.CharField(blank=True, max_length=250, null=True),
                ),
                ("quantity", models.IntegerField(blank=True, default=0, null=True)),
                (
                    "description",
                    models.CharField(blank=True, max_length=250, null=True),
                ),
                ("is_top_save_today", models.BooleanField(default=False)),
                ("is_best_seller", models.BooleanField(default=False)),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="user.category",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Wishlist",
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
                ("added_date", models.DateTimeField(auto_now_add=True)),
                (
                    "product",
                    models.ForeignKey(
                        blank=True,
                        default="",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="user.product",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="user.login",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SubCategory",
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
                    "subcategory",
                    models.CharField(blank=True, max_length=150, null=True),
                ),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="user.category",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SubBanners2",
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
                    "subbanner2",
                    versatileimagefield.fields.VersatileImageField(
                        blank=True, null=True, upload_to="SubBanners/"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="user.product",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SubBanners1",
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
                    "subbanner1",
                    versatileimagefield.fields.VersatileImageField(
                        blank=True, null=True, upload_to="SubBanners/"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="user.product",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Size",
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
                ("size", models.CharField(default=0, max_length=150, null=True)),
                (
                    "product",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="user.product",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="user.login",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="product",
            name="subcategory",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="user.subcategory",
            ),
        ),
        migrations.CreateModel(
            name="Measurements",
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
                    "sleevelength",
                    models.CharField(default=0, max_length=150, null=True),
                ),
                ("chestaround", models.CharField(default=0, max_length=150, null=True)),
                ("waistAround", models.CharField(default=0, max_length=150, null=True)),
                (
                    "LengthTrouser",
                    models.CharField(default=0, max_length=150, null=True),
                ),
                ("hip", models.CharField(default=0, max_length=150, null=True)),
                (
                    "WaistForTrouser",
                    models.CharField(default=0, max_length=150, null=True),
                ),
                ("thighs", models.CharField(default=0, max_length=150, null=True)),
                ("hem", models.CharField(default=0, max_length=150, null=True)),
                (
                    "product",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="user.product",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="user.login",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MainBanner",
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
                    "bannerbig",
                    versatileimagefield.fields.VersatileImageField(
                        blank=True, null=True, upload_to="MainBanner/"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="user.product",
                    ),
                ),
                (
                    "subcategory",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="user.subcategory",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Event",
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
                ("date", models.DateField()),
                (
                    "product",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="user.product",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="user.login",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ChangePassword",
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
                ("forgot_password_token", models.CharField(max_length=100)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("status", models.BooleanField(default=False)),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="user.login",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Cart",
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
                ("product_qty", models.IntegerField(blank=True, null=True)),
                ("added_date", models.DateTimeField(auto_now_add=True)),
                (
                    "product",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="user.product",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="user.login",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AvailableSizes",
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
                ("size", models.CharField(blank=True, max_length=3, null=True)),
                (
                    "product",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="user.product",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AddToCart",
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
                ("added_date", models.DateTimeField(auto_now_add=True)),
                ("quantity", models.IntegerField(default=1, null=True)),
                ("total", models.IntegerField(blank=True, null=True)),
                (
                    "event",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="user.event",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="user.product",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="user.login",
                    ),
                ),
            ],
        ),
    ]
# Generated by Django 4.1.3 on 2022-12-29 04:45

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0011_remove_changepassword_user_delete_login_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="orderdetails",
            old_name="Cart_id",
            new_name="cart_id",
        ),
    ]

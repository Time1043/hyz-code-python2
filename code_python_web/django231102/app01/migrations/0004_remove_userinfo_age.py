# Generated by Django 4.1 on 2023-11-03 01:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app01", "0003_delete_role"),
    ]

    operations = [
        migrations.RemoveField(model_name="userinfo", name="age",),
    ]
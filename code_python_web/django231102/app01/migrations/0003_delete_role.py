# Generated by Django 4.1 on 2023-11-03 01:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app01", "0002_department_role"),
    ]

    operations = [
        migrations.DeleteModel(name="Role",),
    ]
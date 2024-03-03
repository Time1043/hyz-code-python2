# Generated by Django 4.1 on 2023-11-05 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app01", "0002_alter_userinfo_create_time_alter_userinfo_depart"),
    ]

    operations = [
        migrations.CreateModel(
            name="PrettyNum",
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
                ("mobile", models.CharField(max_length=11, verbose_name="手机号码")),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, default=0, max_digits=4, verbose_name="价格"
                    ),
                ),
                (
                    "level",
                    models.SmallIntegerField(
                        choices=[(1, "初级"), (2, "中级"), (3, "高级")],
                        default=1,
                        verbose_name="级别",
                    ),
                ),
                (
                    "status",
                    models.SmallIntegerField(
                        choices=[(0, "未占用"), (1, "已占用")], default=0, verbose_name="状态"
                    ),
                ),
            ],
        ),
    ]
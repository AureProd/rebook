# Generated by Django 5.0.2 on 2024-02-18 18:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="favourite",
            field=models.ManyToManyField(
                blank=True, null=True, related_name="favourite_post", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
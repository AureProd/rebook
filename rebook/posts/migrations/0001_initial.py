# Generated by Django 5.0.2 on 2024-02-19 21:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=1000)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("price", models.IntegerField()),
                ("book_title", models.CharField(max_length=100)),
                ("book_author", models.CharField(max_length=100)),
                ("book_published_at", models.DateField()),
                ("image_1", models.ImageField(blank=True, null=True, upload_to="static/images")),
                ("image_2", models.ImageField(blank=True, null=True, upload_to="static/images")),
                ("image_3", models.ImageField(blank=True, null=True, upload_to="static/images")),
                (
                    "have_in_favourite",
                    models.ManyToManyField(blank=True, related_name="posts_in_favourite", to=settings.AUTH_USER_MODEL),
                ),
                (
                    "seller",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="posts", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
        ),
    ]

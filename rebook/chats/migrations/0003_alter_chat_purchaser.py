# Generated by Django 5.0.2 on 2024-02-19 21:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chats", "0002_alter_chat_purchaser"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="chat",
            name="purchaser",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="chats", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]

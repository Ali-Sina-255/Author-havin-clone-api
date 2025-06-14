# Generated by Django 5.2.1 on 2025-05-26 10:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0001_initial"),
        ("ratings", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rating",
            name="article",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="ratings",
                to="articles.article",
            ),
        ),
    ]

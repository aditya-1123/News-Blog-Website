# Generated by Django 5.0.6 on 2024-07-06 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0006_alter_about_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='about_description',
            field=models.TextField(max_length=255),
        ),
    ]

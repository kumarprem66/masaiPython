# Generated by Django 4.1.10 on 2023-08-13 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dish', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='dishes',
            new_name='dish_items',
        ),
        migrations.AddField(
            model_name='dishes',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
    ]
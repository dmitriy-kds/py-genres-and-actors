# Generated by Django 4.0.2 on 2023-06-18 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='actor',
            old_name='fist_name',
            new_name='first_name',
        ),
    ]
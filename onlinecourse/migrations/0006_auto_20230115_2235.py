# Generated by Django 3.1.3 on 2023-01-15 22:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0005_auto_20230115_2232'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submission',
            old_name='choices',
            new_name='choice',
        ),
    ]
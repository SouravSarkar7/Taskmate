# Generated by Django 3.0.6 on 2020-07-05 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0002_tasklist_manager'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tasklist',
            old_name='manager',
            new_name='manage',
        ),
    ]

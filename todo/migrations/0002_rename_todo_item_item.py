# Generated by Django 3.2.2 on 2021-09-12 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Todo_Item',
            new_name='Item',
        ),
    ]

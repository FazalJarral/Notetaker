# Generated by Django 3.2.2 on 2021-09-17 10:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_item_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
# Generated by Django 3.2 on 2023-04-06 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0006_cat_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cat',
            name='color',
        ),
    ]

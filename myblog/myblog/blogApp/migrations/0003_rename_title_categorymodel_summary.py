# Generated by Django 4.1.6 on 2023-02-24 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0002_alter_postmodel_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categorymodel',
            old_name='title',
            new_name='summary',
        ),
    ]
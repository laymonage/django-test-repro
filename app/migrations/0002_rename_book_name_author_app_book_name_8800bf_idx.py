# Generated by Django 4.2.5 on 2023-09-20 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameIndex(
            model_name='book',
            new_name='app_book_name_8800bf_idx',
            old_fields=('name', 'author'),
        ),
    ]
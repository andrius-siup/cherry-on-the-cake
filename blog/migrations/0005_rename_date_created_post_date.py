# Generated by Django 3.2.5 on 2021-07-30 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_rename_created_date_post_date_created'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='date_created',
            new_name='date',
        ),
    ]

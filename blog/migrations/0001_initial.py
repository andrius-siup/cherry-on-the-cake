# Generated by Django 3.2.5 on 2021-07-28 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=254, null=True)),
                ('content', models.CharField(blank=True, max_length=100000, null=True)),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(blank=True, max_length=25, null=True)),
            ],
        ),
    ]
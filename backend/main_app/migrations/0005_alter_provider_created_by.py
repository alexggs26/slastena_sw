# Generated by Django 4.1.7 on 2023-05-31 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_remove_provider_requisit_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provider',
            name='created_by',
            field=models.IntegerField(verbose_name='main_app.User'),
        ),
    ]
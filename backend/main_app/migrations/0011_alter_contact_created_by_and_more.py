# Generated by Django 4.1.7 on 2023-05-31 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_alter_provider_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='created_by',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='nomenclature',
            name='created_by',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='created_by',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='provider',
            name='created_by',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='provider_requisits',
            name='created_by',
            field=models.IntegerField(null=True),
        ),
    ]
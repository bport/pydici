# Generated by Django 2.2.13 on 2020-12-13 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0021_auto_20201212_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientbill',
            name='lang',
            field=models.CharField(blank=True, choices=[('fr-fr', 'French'), ('en-en', 'English')], max_length=10, null=True, verbose_name='Language'),
        ),
    ]
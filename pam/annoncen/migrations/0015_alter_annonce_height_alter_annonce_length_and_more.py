# Generated by Django 4.0.4 on 2022-06-12 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annoncen', '0014_alter_annonce_kategorie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annonce',
            name='height',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='annonce',
            name='length',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='annonce',
            name='width',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]

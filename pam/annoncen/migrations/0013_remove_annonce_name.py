# Generated by Django 4.0.4 on 2022-06-12 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('annoncen', '0012_alter_kategorie_options_remove_annonce_kategorie_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='annonce',
            name='name',
        ),
    ]

# Generated by Django 4.0.4 on 2022-06-09 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annoncen', '0009_alter_annonce_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='annonce',
            name='available_until',
            field=models.DateField(blank=True, null=True),
        ),
    ]
# Generated by Django 4.0.4 on 2022-06-13 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annoncen', '0015_alter_annonce_height_alter_annonce_length_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='annonce',
            name='latitude',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='annonce',
            name='longitude',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='annonce',
            name='kategorie',
            field=models.ManyToManyField(to='annoncen.kategorie'),
        ),
    ]

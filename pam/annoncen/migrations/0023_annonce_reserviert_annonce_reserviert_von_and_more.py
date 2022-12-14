# Generated by Django 4.0.4 on 2022-06-28 23:55

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('annoncen', '0022_annonce_adresszusatz_profile_adresszusatz_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='annonce',
            name='reserviert',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='annonce',
            name='reserviert_von',
            field=models.ManyToManyField(blank=True, default=None, related_name='reservierer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='annonce',
            name='author',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='annonce',
            name='available_until',
            field=models.DateField(default=datetime.date(2022, 9, 29)),
        ),
    ]

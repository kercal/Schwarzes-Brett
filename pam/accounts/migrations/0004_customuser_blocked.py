# Generated by Django 4.0.4 on 2022-07-11 16:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_customuser_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='blocked',
            field=models.ManyToManyField(related_name='blocked_by', to=settings.AUTH_USER_MODEL),
        ),
    ]

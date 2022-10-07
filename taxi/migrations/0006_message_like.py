# Generated by Django 4.0.2 on 2022-10-05 06:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0005_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]

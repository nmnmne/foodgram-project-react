# Generated by Django 3.2.3 on 2023-08-29 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_favorite_recipes'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_subscribed',
            field=models.BooleanField(default=False, verbose_name='Подписан'),
        ),
    ]

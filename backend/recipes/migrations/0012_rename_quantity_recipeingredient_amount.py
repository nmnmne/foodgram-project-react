# Generated by Django 3.2.3 on 2023-08-29 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0011_ingredient_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipeingredient',
            old_name='quantity',
            new_name='amount',
        ),
    ]

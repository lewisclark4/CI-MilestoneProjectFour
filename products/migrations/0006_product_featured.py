# Generated by Django 3.1.3 on 2020-12-01 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]

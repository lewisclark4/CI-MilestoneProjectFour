# Generated by Django 3.1.3 on 2020-12-16 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='address1',
            new_name='address_1',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='address2',
            new_name='address_2',
        ),
    ]

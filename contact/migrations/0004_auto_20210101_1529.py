# Generated by Django 3.1.3 on 2021-01-01 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_auto_20201229_1629'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscription',
            old_name='email',
            new_name='email_address',
        ),
    ]

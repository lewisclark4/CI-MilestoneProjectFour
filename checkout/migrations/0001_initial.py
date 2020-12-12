# Generated by Django 3.1.3 on 2020-12-12 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0007_auto_20201205_2214'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(editable=False, max_length=32)),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('address1', models.CharField(max_length=80)),
                ('address2', models.CharField(blank=True, max_length=80, null=True)),
                ('city', models.CharField(max_length=40)),
                ('county', models.CharField(blank=True, max_length=80, null=True)),
                ('country', models.CharField(max_length=40)),
                ('postcode', models.CharField(blank=True, max_length=20, null=True)),
                ('delivery_cost', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('order_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('grand_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='OrderLineItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('lineitem_total', models.DecimalField(decimal_places=2, editable=False, max_digits=6)),
                ('colour', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.colour')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lineitems', to='checkout.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.product')),
            ],
        ),
    ]
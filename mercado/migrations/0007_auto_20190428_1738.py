# Generated by Django 2.0.13 on 2019-04-28 20:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mercado', '0006_auto_20190428_1620'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendasrealizadas',
            old_name='produto_id',
            new_name='venda_id',
        ),
    ]

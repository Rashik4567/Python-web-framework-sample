# Generated by Django 3.0.7 on 2020-07-03 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20200703_1639'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='Rating',
        ),
    ]

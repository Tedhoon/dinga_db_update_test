# Generated by Django 2.2.7 on 2020-01-03 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0004_auto_20200103_1715'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publicdata',
            name='pb_update_check',
        ),
    ]

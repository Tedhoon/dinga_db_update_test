# Generated by Django 2.2.7 on 2020-01-04 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0008_publicdata_pb_update_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publicdata',
            name='pb_update_date',
        ),
    ]
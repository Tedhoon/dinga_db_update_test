# Generated by Django 2.2.7 on 2020-01-04 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0007_remove_publicdata_pb_update_check'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicdata',
            name='pb_update_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

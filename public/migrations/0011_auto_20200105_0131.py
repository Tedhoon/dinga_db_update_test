# Generated by Django 2.2.7 on 2020-01-04 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0010_publicdata_pb_update_check'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicupdate',
            name='pb_dinga_agerange',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='publicupdate',
            name='pb_dinga_type',
            field=models.TextField(blank=True, null=True),
        ),
    ]

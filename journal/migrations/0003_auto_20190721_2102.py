# Generated by Django 2.2.1 on 2019-07-21 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0002_note_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='content',
            field=models.TextField(default='this is the default text'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='note',
            name='word_count',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
    ]

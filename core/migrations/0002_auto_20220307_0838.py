# Generated by Django 3.2 on 2022-03-07 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='base_ptr',
        ),
        migrations.DeleteModel(
            name='Base',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]

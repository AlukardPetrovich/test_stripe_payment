# Generated by Django 2.2.27 on 2022-09-19 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stripe_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='item',
            new_name='name',
        ),
    ]
# Generated by Django 2.2.27 on 2022-09-19 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.TextField(verbose_name='Назвние товара')),
                ('description', models.TextField(verbose_name='Описание товара')),
                ('price', models.IntegerField(verbose_name='Стоимость товара')),
            ],
        ),
    ]

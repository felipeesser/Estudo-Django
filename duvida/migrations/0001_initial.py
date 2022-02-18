# Generated by Django 3.2.9 on 2021-12-07 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Duvida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(db_index=True, max_length=70, unique=True)),
                ('slug', models.SlugField(max_length=70)),
            ],
            options={
                'db_table': 'duvida',
            },
        ),
    ]
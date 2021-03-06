# Generated by Django 3.2.9 on 2021-12-04 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(db_index=True, max_length=70, unique=True)),
                ('slug', models.SlugField(max_length=70)),
                ('genero', models.CharField(max_length=200)),
                ('imagem', models.CharField(blank=True, max_length=70)),
            ],
            options={
                'db_table': 'filme',
            },
        ),
    ]

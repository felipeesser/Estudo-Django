# Generated by Django 3.2.9 on 2021-12-08 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Promocao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('promocao', models.CharField(db_index=True, max_length=70)),
                ('slug', models.SlugField(max_length=70)),
                ('corpo', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'promocao',
            },
        ),
    ]

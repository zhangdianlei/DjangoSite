# Generated by Django 3.0.4 on 2020-03-13 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0005_movie_mins'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='official_site',
            field=models.TextField(),
        ),
    ]

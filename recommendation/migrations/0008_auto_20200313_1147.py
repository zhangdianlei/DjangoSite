# Generated by Django 3.0.4 on 2020-03-13 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0007_auto_20200313_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.TextField(),
        ),
    ]
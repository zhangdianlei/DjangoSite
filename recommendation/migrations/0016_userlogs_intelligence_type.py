# Generated by Django 3.0.4 on 2020-04-22 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0015_auto_20200421_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlogs',
            name='intelligence_type',
            field=models.CharField(default='动向情报', max_length=64),
        ),
    ]
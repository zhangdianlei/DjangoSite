# Generated by Django 3.0.4 on 2020-04-21 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0011_auto_20200421_1544'),
    ]

    operations = [
        migrations.CreateModel(
            name='Intelligence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intelligence_id', models.CharField(max_length=128)),
                ('intelligence_type', models.CharField(default='动向情报', max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=128)),
                ('intelligence_id', models.CharField(max_length=128)),
            ],
        ),
    ]

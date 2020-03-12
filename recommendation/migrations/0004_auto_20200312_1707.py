# Generated by Django 3.0.4 on 2020-03-12 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0003_auto_20200312_1637'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.CharField(max_length=64)),
                ('name', models.CharField(max_length=128)),
                ('alias', models.CharField(max_length=128)),
                ('actors', models.TextField()),
                ('cover', models.TextField()),
                ('director', models.TextField()),
                ('douban_score', models.CharField(max_length=10)),
                ('double_vote', models.CharField(max_length=10)),
                ('genres', models.CharField(max_length=128)),
                ('imdb_id', models.CharField(max_length=128)),
                ('language', models.CharField(max_length=64)),
                ('official_site', models.CharField(max_length=128)),
                ('regions', models.CharField(max_length=64)),
                ('release_date', models.CharField(max_length=64)),
                ('slug', models.CharField(max_length=32)),
                ('storyline', models.TextField()),
                ('tags', models.TextField()),
                ('year', models.CharField(max_length=32)),
                ('actor_ids', models.TextField()),
                ('director_ids', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserMovieLogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=128)),
                ('movie_id', models.CharField(max_length=128)),
                ('time', models.TimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='user_name',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='user_age',
            new_name='age',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_phone',
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default=1, max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(default=1, max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='remark',
            field=models.CharField(default=1, max_length=64),
            preserve_default=False,
        ),
    ]

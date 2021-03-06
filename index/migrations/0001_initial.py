# Generated by Django 2.2.7 on 2019-11-24 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShortUrlModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('hash_code', models.CharField(blank=True, max_length=100)),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('private', models.BooleanField(default=False)),
                ('password', models.CharField(max_length=50)),
                ('permanent', models.BooleanField(default=False)),
                ('expire_time', models.DateTimeField()),
                ('custom', models.BooleanField(default=False)),
                ('title', models.CharField(blank=True, max_length=200)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('thumbnail', models.ImageField(blank=True, upload_to='thumbnails')),
            ],
        ),
    ]

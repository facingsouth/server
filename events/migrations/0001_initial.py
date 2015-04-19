# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=30, blank=True)),
                ('description', models.TextField(default=b'', blank=True)),
                ('location_lon', models.DecimalField(max_digits=8, decimal_places=5)),
                ('location_lat', models.DecimalField(max_digits=8, decimal_places=5)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('started_on', models.DateTimeField()),
                ('group_size', models.IntegerField()),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Follower',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('followed_on', models.DateTimeField(auto_now_add=True)),
                ('event', models.ForeignKey(to='events.Event')),
                ('follower', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-02-27 09:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compileinfo',
            fields=[
                ('solution_id', models.IntegerField(primary_key=True, serialize=False)),
                ('error', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'compileinfo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('contest_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('defunct', models.CharField(max_length=1)),
                ('description', models.TextField(blank=True, null=True)),
                ('private', models.IntegerField()),
                ('langmask', models.IntegerField()),
                ('password', models.CharField(max_length=16)),
            ],
            options={
                'db_table': 'contest',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ContestProblem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem_id', models.IntegerField()),
                ('contest_id', models.IntegerField(blank=True, null=True)),
                ('title', models.CharField(max_length=200)),
                ('num', models.IntegerField()),
            ],
            options={
                'db_table': 'contest_problem',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Custominput',
            fields=[
                ('solution_id', models.IntegerField(primary_key=True, serialize=False)),
                ('input_text', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'custominput',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Loginlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=48)),
                ('password', models.CharField(blank=True, max_length=40, null=True)),
                ('ip', models.CharField(blank=True, max_length=100, null=True)),
                ('time', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'loginlog',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('mail_id', models.AutoField(primary_key=True, serialize=False)),
                ('to_user', models.CharField(max_length=48)),
                ('from_user', models.CharField(max_length=48)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField(blank=True, null=True)),
                ('new_mail', models.IntegerField()),
                ('reply', models.IntegerField(blank=True, null=True)),
                ('in_date', models.DateTimeField(blank=True, null=True)),
                ('defunct', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'mail',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('news_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.CharField(max_length=48)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('time', models.DateTimeField()),
                ('importance', models.IntegerField()),
                ('defunct', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'news',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Online',
            fields=[
                ('hash', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('ip', models.CharField(max_length=20)),
                ('ua', models.CharField(max_length=255)),
                ('refer', models.CharField(blank=True, max_length=255, null=True)),
                ('lastmove', models.IntegerField()),
                ('firsttime', models.IntegerField(blank=True, null=True)),
                ('uri', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'online',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Privilege',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=48)),
                ('rightstr', models.CharField(max_length=30)),
                ('defunct', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'privilege',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('problem_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('input', models.TextField(blank=True, null=True)),
                ('output', models.TextField(blank=True, null=True)),
                ('sample_input', models.TextField(blank=True, null=True)),
                ('sample_output', models.TextField(blank=True, null=True)),
                ('spj', models.CharField(max_length=1)),
                ('hint', models.TextField(blank=True, null=True)),
                ('source', models.CharField(blank=True, max_length=100, null=True)),
                ('in_date', models.DateTimeField(blank=True, null=True)),
                ('time_limit', models.IntegerField()),
                ('memory_limit', models.IntegerField()),
                ('defunct', models.CharField(max_length=1)),
                ('accepted', models.IntegerField(blank=True, null=True)),
                ('submit', models.IntegerField(blank=True, null=True)),
                ('solved', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'problem',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('rid', models.AutoField(primary_key=True, serialize=False)),
                ('author_id', models.CharField(max_length=48)),
                ('time', models.DateTimeField()),
                ('content', models.TextField()),
                ('topic_id', models.IntegerField()),
                ('status', models.IntegerField()),
                ('ip', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'reply',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Runtimeinfo',
            fields=[
                ('solution_id', models.IntegerField(primary_key=True, serialize=False)),
                ('error', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'runtimeinfo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sim',
            fields=[
                ('s_id', models.IntegerField(primary_key=True, serialize=False)),
                ('sim_s_id', models.IntegerField(blank=True, null=True)),
                ('sim', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'sim',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('solution_id', models.AutoField(primary_key=True, serialize=False)),
                ('problem_id', models.IntegerField()),
                ('user_id', models.CharField(max_length=48)),
                ('time', models.IntegerField()),
                ('memory', models.IntegerField()),
                ('in_date', models.DateTimeField()),
                ('result', models.SmallIntegerField()),
                ('language', models.IntegerField()),
                ('ip', models.CharField(max_length=46)),
                ('contest_id', models.IntegerField(blank=True, null=True)),
                ('valid', models.IntegerField()),
                ('num', models.IntegerField()),
                ('code_length', models.IntegerField()),
                ('judgetime', models.DateTimeField(blank=True, null=True)),
                ('pass_rate', models.DecimalField(decimal_places=2, max_digits=3)),
                ('lint_error', models.IntegerField()),
                ('judger', models.CharField(max_length=16)),
            ],
            options={
                'db_table': 'solution',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SourceCode',
            fields=[
                ('solution_id', models.IntegerField(primary_key=True, serialize=False)),
                ('source', models.TextField()),
            ],
            options={
                'db_table': 'source_code',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SourceCodeUser',
            fields=[
                ('solution_id', models.IntegerField(primary_key=True, serialize=False)),
                ('source', models.TextField()),
            ],
            options={
                'db_table': 'source_code_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('tid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=60)),
                ('status', models.IntegerField()),
                ('top_level', models.IntegerField()),
                ('cid', models.IntegerField(blank=True, null=True)),
                ('pid', models.IntegerField()),
                ('author_id', models.CharField(max_length=48)),
            ],
            options={
                'db_table': 'topic',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.CharField(max_length=48, primary_key=True, serialize=False)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('submit', models.IntegerField(blank=True, null=True)),
                ('solved', models.IntegerField(blank=True, null=True)),
                ('defunct', models.CharField(max_length=1)),
                ('ip', models.CharField(max_length=20)),
                ('accesstime', models.DateTimeField(blank=True, null=True)),
                ('volume', models.IntegerField()),
                ('language', models.IntegerField()),
                ('password', models.CharField(blank=True, max_length=32, null=True)),
                ('reg_time', models.DateTimeField(blank=True, null=True)),
                ('nick', models.CharField(max_length=100)),
                ('school', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
    ]

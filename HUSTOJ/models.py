# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Compileinfo(models.Model):
    solution_id = models.IntegerField(primary_key=True)
    error = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'compileinfo'


class Contest(models.Model):
    contest_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    defunct = models.CharField(max_length=1)
    description = models.TextField(blank=True, null=True)
    private = models.IntegerField()
    langmask = models.IntegerField()
    password = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'contest'


class ContestProblem(models.Model):
    problem_id = models.IntegerField()
    contest_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=200)
    num = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'contest_problem'


class Custominput(models.Model):
    solution_id = models.IntegerField(primary_key=True)
    input_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'custominput'


class Loginlog(models.Model):
    user_id = models.CharField(max_length=48)
    password = models.CharField(max_length=40, blank=True, null=True)
    ip = models.CharField(max_length=100, blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loginlog'


class Mail(models.Model):
    mail_id = models.AutoField(primary_key=True)
    to_user = models.CharField(max_length=48)
    from_user = models.CharField(max_length=48)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    new_mail = models.IntegerField()
    reply = models.IntegerField(blank=True, null=True)
    in_date = models.DateTimeField(blank=True, null=True)
    defunct = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'mail'


class News(models.Model):
    news_id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=48)
    title = models.CharField(max_length=200)
    content = models.TextField()
    time = models.DateTimeField()
    importance = models.IntegerField()
    defunct = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'news'


class Online(models.Model):
    hash = models.CharField(primary_key=True, max_length=32)
    ip = models.CharField(max_length=20)
    ua = models.CharField(max_length=255)
    refer = models.CharField(max_length=255, blank=True, null=True)
    lastmove = models.IntegerField()
    firsttime = models.IntegerField(blank=True, null=True)
    uri = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'online'


class Privilege(models.Model):
    user_id = models.CharField(max_length=48)
    rightstr = models.CharField(max_length=30)
    defunct = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'privilege'


class Problem(models.Model):
    problem_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    input = models.TextField(blank=True, null=True)
    output = models.TextField(blank=True, null=True)
    sample_input = models.TextField(blank=True, null=True)
    sample_output = models.TextField(blank=True, null=True)
    spj = models.CharField(max_length=1)
    hint = models.TextField(blank=True, null=True)
    source = models.CharField(max_length=100, blank=True, null=True)
    in_date = models.DateTimeField(blank=True, null=True)
    time_limit = models.IntegerField()
    memory_limit = models.IntegerField()
    defunct = models.CharField(max_length=1)
    accepted = models.IntegerField(blank=True, null=True)
    submit = models.IntegerField(blank=True, null=True)
    solved = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'problem'


class Reply(models.Model):
    rid = models.AutoField(primary_key=True)
    author_id = models.CharField(max_length=48)
    time = models.DateTimeField()
    content = models.TextField()
    topic_id = models.IntegerField()
    status = models.IntegerField()
    ip = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'reply'


class Runtimeinfo(models.Model):
    solution_id = models.IntegerField(primary_key=True)
    error = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'runtimeinfo'


class Sim(models.Model):
    s_id = models.IntegerField(primary_key=True)
    sim_s_id = models.IntegerField(blank=True, null=True)
    sim = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sim'


class Solution(models.Model):
    solution_id = models.AutoField(primary_key=True)
    problem_id = models.IntegerField()
    user_id = models.CharField(max_length=48)
    time = models.IntegerField()
    memory = models.IntegerField()
    in_date = models.DateTimeField()
    result = models.SmallIntegerField()
    language = models.IntegerField()
    ip = models.CharField(max_length=46)
    contest_id = models.IntegerField(blank=True, null=True)
    valid = models.IntegerField()
    num = models.IntegerField()
    code_length = models.IntegerField()
    judgetime = models.DateTimeField(blank=True, null=True)
    pass_rate = models.DecimalField(max_digits=3, decimal_places=2)
    lint_error = models.IntegerField()
    judger = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'solution'


class SourceCode(models.Model):
    solution_id = models.IntegerField(primary_key=True)
    source = models.TextField()

    class Meta:
        managed = False
        db_table = 'source_code'


class SourceCodeUser(models.Model):
    solution_id = models.IntegerField(primary_key=True)
    source = models.TextField()

    class Meta:
        managed = False
        db_table = 'source_code_user'


class Topic(models.Model):
    tid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=60)
    status = models.IntegerField()
    top_level = models.IntegerField()
    cid = models.IntegerField(blank=True, null=True)
    pid = models.IntegerField()
    author_id = models.CharField(max_length=48)

    class Meta:
        managed = False
        db_table = 'topic'


class Users(models.Model):
    user_id = models.CharField(primary_key=True, max_length=48)
    email = models.CharField(max_length=100, blank=True, null=True)
    submit = models.IntegerField(blank=True, null=True)
    solved = models.IntegerField(blank=True, null=True)
    defunct = models.CharField(max_length=1)
    ip = models.CharField(max_length=20)
    accesstime = models.DateTimeField(blank=True, null=True)
    volume = models.IntegerField()
    language = models.IntegerField()
    password = models.CharField(max_length=32, blank=True, null=True)
    reg_time = models.DateTimeField(blank=True, null=True)
    nick = models.CharField(max_length=100)
    school = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'users'


# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-04-05 13:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('content', models.TextField(verbose_name='评论内容')),
            ],
            options={
                'verbose_name': '关于自己评论',
                'verbose_name_plural': '关于自己评论',
                'ordering': ['create_date'],
            },
        ),
        migrations.CreateModel(
            name='ArticleComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('content', models.TextField(verbose_name='评论内容')),
            ],
            options={
                'verbose_name': '文章评论',
                'verbose_name_plural': '文章评论',
                'ordering': ['create_date'],
            },
        ),
        migrations.CreateModel(
            name='CommentUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=20, verbose_name='昵称')),
                ('email', models.CharField(max_length=30, verbose_name='邮箱')),
                ('address', models.CharField(max_length=200, verbose_name='地址')),
            ],
        ),
        migrations.CreateModel(
            name='MessageComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('content', models.TextField(verbose_name='评论内容')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messagecomment_related', to='comment.CommentUser', verbose_name='评论人')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='messagecomment_child_comments', to='comment.MessageComment', verbose_name='父评论')),
                ('rep_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='messagecomment_rep_comments', to='comment.MessageComment', verbose_name='回复')),
            ],
            options={
                'verbose_name': '给我留言',
                'verbose_name_plural': '给我留言',
                'ordering': ['create_date'],
            },
        ),
        migrations.AddField(
            model_name='articlecomment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articlecomment_related', to='comment.CommentUser', verbose_name='评论人'),
        ),
    ]

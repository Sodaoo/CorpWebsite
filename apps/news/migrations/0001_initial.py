# Generated by Django 2.0.8 on 2020-08-05 16:51

import DjangoUeditor.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='', max_length=5000, verbose_name='文章标题')),
                ('content_brief', models.TextField(max_length=50000, verbose_name='文章描述')),
                ('content', models.TextField(max_length=101000, verbose_name='文章内容')),
                ('contents', DjangoUeditor.models.UEditorField(default='', verbose_name='内容')),
                ('click_num', models.IntegerField(default=0, verbose_name='点击数')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='文章发表时间')),
            ],
            options={
                'verbose_name': '新闻模块',
                'verbose_name_plural': '新闻模块',
            },
        ),
    ]

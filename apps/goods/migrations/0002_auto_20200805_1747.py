# Generated by Django 2.0.8 on 2020-08-05 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goods',
            name='market_price',
        ),
        migrations.RemoveField(
            model_name='goods',
            name='ship_free',
        ),
        migrations.AlterField(
            model_name='goods',
            name='goods_brief',
            field=models.TextField(max_length=500, verbose_name='简短描述'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='goods_sn',
            field=models.CharField(default='', max_length=50, verbose_name='产品 ID'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='name',
            field=models.CharField(max_length=100, verbose_name='产品名称'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='sold_num',
            field=models.IntegerField(default=0, verbose_name='销售量'),
        ),
    ]

# Generated by Django 2.2.6 on 2019-12-22 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_auto_20191222_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='pay_status',
            field=models.CharField(choices=[('1', '未支付'), ('2', '未发货'), ('3', '已发货'), ('4', '确认收货'), ('5', '已过期'), ('6', '已取消')], default='1', max_length=30, verbose_name='订单状态'),
        ),
    ]

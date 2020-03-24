# Generated by Django 2.2.6 on 2019-12-17 08:58

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0008_auto_20191216_1124'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0004_auto_20191217_1642'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='goodid',
            new_name='good',
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='userid',
            new_name='user',
        ),
        migrations.AlterUniqueTogether(
            name='cart',
            unique_together={('good', 'user')},
        ),
    ]

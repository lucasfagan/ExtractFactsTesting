# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-29 20:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('claimapp', '0002_authgroup_authgrouppermissions_authpermission_authuser_authusergroups_authuseruserpermissions_django'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='speak',
            table='Speak',
        ),
    ]
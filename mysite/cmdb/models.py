 # -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class message(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=15)


class itzc(models.Model):
    jqm = models.CharField(max_length=20)
    ipaddr = models.CharField(max_length=35)
    user = models.CharField(max_length=35)
    userpwd = models.CharField(max_length=35)
    addr = models.CharField(max_length=45)
    paydate = models.CharField(max_length=35)

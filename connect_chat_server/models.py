# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Message(models.Model):
    message_txt = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')




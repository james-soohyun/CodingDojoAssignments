# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
	first = models.CharField(max_length = 200)
	last = models.CharField(max_length = 200)
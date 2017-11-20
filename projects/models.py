# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
	"""Model of Project. It's a big section of the primple"""
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=256)
	create_date = models.DateTimeField(auto_now_add=True)
	change_date = models.DateTimeField(auto_now=True)
	#creator = models.ForeignKey(settings.AUTH_USER_MODEL)
	creator = models.ForeignKey(User)


	def __str__(self):
		return self.name

class Section(models.Model):
	"""Model of Section. It's a little section of a project"""
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=256)
	create_date = models.DateTimeField(auto_now_add=True)
	change_date = models.DateTimeField(auto_now=True)
	creator = models.ForeignKey(User)


	def __str__(self):
		return self.name

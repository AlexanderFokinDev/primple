# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class KnowledgeBase(models.Model):
	#id = models.IntegerField(primary_key=True)
	question = models.TextField()
	response = models.TextField()

	def __str__(self):
		return self.question
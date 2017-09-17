# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class KnowledgeBase(models.Model):
	"""Model of knowledge base. Consist from entries with question and responce"""

	#id = models.IntegerField(primary_key=True)
	question = models.TextField()
	response = models.TextField()

	#def __init__(self, question, response):
		#self.id = id
	#	self.question = question
	#	self.response = response

	def __str__(self):
		return self.question
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from projects.models import Project
from projects.models import Section

# Create your models here.
class KnowledgeBase(models.Model):
	"""Model of knowledge base. Consist from entries with question and responce"""

	#id = models.IntegerField(primary_key=True)
	question = models.TextField()
	response = models.TextField(blank=True)
	short_description = models.CharField(blank=True, max_length=256)
	create_date = models.DateTimeField(auto_now_add=True)
	change_date = models.DateTimeField(auto_now=True)
	project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True)
	key_words = models.CharField(blank=True, max_length=256)
	author_query = models.ForeignKey(User, verbose_name='Author of query', related_name='kb_queries')
	author_answer = models.ForeignKey(User, verbose_name='Author of answer', related_name='kb_answeres')
	section = models.ForeignKey(Section, on_delete=models.CASCADE, blank=True)

	#def __init__(self, question, response):
		#self.id = id
	#	self.question = question
	#	self.response = response

	def __str__(self):
		return self.question
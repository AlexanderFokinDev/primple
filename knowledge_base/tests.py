# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from knowledge_base.models import KnowledgeBase

# Create your tests here.

class KnowledgeBaseTests(TestCase):
	"""Knowledge model tests"""

	def test_str(self):
		entry = KnowledgeBase("Test question","")
		self.assertEquals(str(entry), "Test question")

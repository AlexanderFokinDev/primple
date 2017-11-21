# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Project
from .models import Section

# Register your models here.
admin.site.register(Project)
admin.site.register(Section)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Puppies(models.Model):
	name = models.CharField(db_index=True, blank=False, null=False, max_length=255)
	age = models.IntegerField(default=0)
	breed = models.CharField(db_index=True, blank=False, null=False, max_length=50)
	color = models.CharField(db_index=True, blank=False, null=False, max_length=50)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

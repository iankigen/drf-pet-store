# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Puppies


class PuppyTestCase(TestCase):
	def setUp(self):
		pass

	def test_create_puppies(self):
		puppies_count_before = Puppies.objects.count()
		puppy = Puppies.objects.create(name='Casper', age=3, breed='Bull Dog', color='Black')
		self.assertEqual(puppy.name, 'Casper')
		self.assertEqual(puppies_count_before + 1, Puppies.objects.count())

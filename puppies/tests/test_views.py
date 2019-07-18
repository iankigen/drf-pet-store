# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from django.test import TestCase, Client
from django.urls import reverse

from puppies.models import Puppies
from puppies.serializers import PuppiesSerializer


class PuppiesViewsTestCase(TestCase):
	def setUp(self):
		self.client = Client()
		self.puppy = Puppies.objects.create(name='test', age=1, color='brown', breed='german shepherd')
		self.puppies = Puppies.objects.all()

	def test_get_all_puppies(self):
		res = self.client.get(reverse('puppies-list'))
		serializer = PuppiesSerializer(self.puppies, many=True)
		self.assertEqual(res.data['results'], serializer.data)
		self.assertEqual(res.status_code, 200)

	def test_get_one_puppy(self):
		res = self.client.get(reverse('puppies-detail', args=[self.puppy.id]))
		serializer = PuppiesSerializer(self.puppy)
		self.assertEqual(res.data, serializer.data)
		self.assertEqual(res.status_code, 200)

	def test_can_add_a_puppy(self):
		count_before = self.puppies.count()
		res = self.client.post(reverse('puppies-list'), data={
			'name': 'test',
			'breed': 'gs',
			'age': 1,
			'color': 'test'
		})
		self.assertEqual(self.puppies.count(), count_before + 1)
		self.assertEqual(res.status_code, 201)

	def test_can_delete_a_puppy(self):
		count_before = self.puppies.count()
		res = self.client.delete(reverse('puppies-detail', args=[self.puppy.id]))
		self.assertEqual(self.puppies.count(), count_before - 1)
		self.assertEqual(res.status_code, 204)

	def test_can_update_a_puppy(self):
		res = self.client.put(reverse('puppies-detail', args=[self.puppy.id]), data={
			'name': 'test',
			'breed': 'gs',
			'age': 1,
			'color': 'test'
		}, content_type='application/json')
		self.assertEqual(Puppies.objects.get(pk=self.puppy.id).color, 'test')
		self.assertEqual(res.status_code, 200)

	def test_get_non_existing_puppy(self):
		res = self.client.get(reverse('puppies-detail', args=[10000]))
		self.assertEqual(res.status_code, 404)

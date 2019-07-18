# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter

from .models import Puppies
from .serializers import PuppiesSerializer
from .paginantion import PuppiesPaginantion


class PuppiesViewSet(ModelViewSet):
	queryset = Puppies.objects.all()
	serializer_class = PuppiesSerializer
	permission_classes = []
	http_method_names = ('get', 'post', 'put', 'delete')
	filter_backends = [SearchFilter]
	search_fields = ('name', 'color', 'breed', 'age')
	pagination_class = PuppiesPaginantion

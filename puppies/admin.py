# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Puppies


class PuppiesAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'color', 'breed', 'created_at')
	list_filter = ('breed', 'color', 'name')
	ordering = ('name', 'color', 'id', 'breed')
	search_fields = ('name', 'color', 'id', 'breed')


admin.site.register(Puppies, PuppiesAdmin)

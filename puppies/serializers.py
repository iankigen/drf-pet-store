from rest_framework import serializers

from .models import Puppies


class PuppiesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Puppies
		fields = ('id', 'name', 'color', 'breed', 'created_at', 'updated_at')
		extra_kwargs = {
			'id': {'read_only': True},
			'created_at': {'read_only': True},
			'updated_at': {'read_only': True},
		}

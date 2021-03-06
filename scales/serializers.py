from rest_framework import serializers
from .models import Point, Scale, Raise

import logging

logger = logging.getLogger(__name__)


class PointSerializer(serializers.ModelSerializer):

	class Meta:
		model  = Point
		fields = '__all__'
		read_only_fields = ('timestamp',)

class ScaleSerializer(serializers.ModelSerializer):
	class Meta:
		model  = Scale
		fields = '__all__'
		read_only_fields = ('timestamp',)


class RaiseSerializer(serializers.Serializer):

	scale_id	= serializers.RelatedField(source='Scale',read_only=True)
#	scale 		= serializers.IntegerField()
	quantity	= serializers.IntegerField()
	amount  	= serializers.DecimalField(max_digits=30, decimal_places=15)
	base64		= serializers.CharField()
	codigo		= serializers.CharField()
#	timestamp	= serializers.TimeField()

	def create(self, validated_data):


		return Raise.objects.create(**validated_data)

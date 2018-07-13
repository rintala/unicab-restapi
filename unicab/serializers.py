from django.contrib.auth.models import User
from rest_framework import serializers
import sys
sys.path.append('..')
from usermanager.models import Users
from rest_framework import viewsets

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = Users
		fields = '__all__'
		lookup_field = 'email'
		extra_kwargs = {
            		'url': {'lookup_field': 'email'}
		}

class DistanceSerializer(serializers.Serializer):

	initial_email = serializers.CharField(max_length=35)
	initial_latitude = serializers.DecimalField(max_digits=10, decimal_places=6)
	initial_longitude = serializers.DecimalField(max_digits=10, decimal_places=6)
	other_email = serializers.CharField(max_length=35)
	other_latitude = serializers.DecimalField(max_digits=10, decimal_places=6)
	other_longitude = serializers.DecimalField(max_digits=10, decimal_places=6)
	distance = serializers.DecimalField(max_digits=10, decimal_places=6)

class ChangeIsSearchingSerializer(serializers.Serializer):
	""" Serializer for change of is_searching variable """
	old_is_searching = serializers.CharField(required=True)
	new_is_searching = serializers.CharField(required=True)



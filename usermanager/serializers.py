from rest_framework import serializers
from .models import Users
from .models import Trips

class UsersSerializer(serializers.ModelSerializer):
	class Meta:
        	model = Users
        	fields = ("id","first_name", "last_name", "email", "date_of_birth", "phone_verified", "faculty", "home_adress","nr_of_trips_done", "avg_rating", "profile_picture", "description")

class TripsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Trips
		fields = ("id")


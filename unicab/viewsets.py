
#from django.contrib.auth.models import Users
# Add this line to the beginning of relative.py file
import sys
sys.path.append('..')
from django.http import JsonResponse
from usermanager.models import Users
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
#IMPORT YOUR SERIALIZERS
from .serializers import *
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.list import ListView
#@csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.decorators import detail_route
import json
from geopy.distance import distance as geopydistance

from collections import OrderedDict
#from rest_framework.permissions import IsAuthenticated

@method_decorator(csrf_exempt, name='dispatch')
class UserViewSet(viewsets.ModelViewSet):
	"""
	A simple Viewset for viewing and editing accounts.
	"""
	queryset = Users.objects.all()
	serializer_class = UserSerializer

#@csrf_exempt
@method_decorator(csrf_exempt, name='dispatch')
class TripsViewSet(viewsets.ModelViewSet):
	queryset = Users.objects.all()
	serializer_class = UserSerializer

#@csrf_exempt
@method_decorator(csrf_exempt, name='dispatch')
class UserInDatabase(viewsets.ModelViewSet):
	#try:
	def get_queryset(self):
		emailIn = self.request.query_params.get('email')
		queryset=Users.objects.filter(email=emailIn)
		if queryset.exists():
			return queryset
		else:
			raise Http404
			#return Response({'message':'False'},404).build();
			#return JsonResponse(status=status.HTTP_404_NOT_FOUND)
		#except Users.DoesNotExist:
		#	raise Http404
		#return queryset
		#queryset=request
		#except Users.DoesNotExist:
		#queryset=None
		#if queryset.exists():
		#	print("YESS")
		#else:
		#	print("no")
	#queryset=queryset[1]
	#for e in queryset:
	#	print(e.email)
	#serializer_class = ''
	serializer_class = UserSerializer
	#permission_classes = (IsAuthenticated,)

	@csrf_exempt
	def post(self, request, format=None):
		serializer = SnippetSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	queryset = Users.objects.all()

	def update(self, request, *args, **kwargs):
		instance = self.get_object()
		instance.is_searching = request.data.get("is_searching")
		instance.save()

		serializer = self.get_serializer(instance)
		serializer.is_valid(raise_exception=True)
		self.perform_update(serializer)

		return Response(serializer.data)	
#def get(self, request):
	#	queryset = Users.object.all()
	#	user=queryset[1]
	#	serializer = UserSerializer(user, many=True)
	#	return Response(serializer.data)
	#queryset = Users.objects.all()
	#queryset = ''
	#def get_queryset(self):
		#original qs
		#qs = super().get_queryset()
        	#filter by a variable captured from url, for example
        	#return qs.filter(name__startswith=self.kwargs.email)

class DistanceView(viewsets.ModelViewSet):
	#queryset = Users.objects.filter(is_searching=True)
	queryset = Users.objects.all()
	serializer_class = UserSerializer
	lookup_field = 'email'

	def retrieve(self, request, *args, **kwargs):
		email = kwargs.get('email', None)
		#user_id = Users.objects.get(email=email)
		#self.queryset = Users.objects.filter(email=email)
		#self.queryset = Users.objects.all()
		thequeryset = self.get_queryset()
		theUserSearching = thequeryset.get(email=email)
		#queryset = self.get_queryset()
		#qsTheUserSearching = queryset.get(email=email)
		the_initial_latitude = theUserSearching.home_latitude
		the_initial_longitude = theUserSearching.home_longitude
		qsOtherUsersSearching=thequeryset.filter(is_searching=True)
		output=[]
		for otherUser in qsOtherUsersSearching:
			coords_1 = (the_initial_latitude, the_initial_longitude)
			coords_2 = (otherUser.home_latitude, otherUser.home_longitude)
			euclidian_distance = geopydistance(coords_1, coords_2).km
			json_obj = dict(
            			initial_email = email,
				initial_latitude = the_initial_latitude,
				initial_longitude = the_initial_longitude,
				other_email = otherUser.email,
				other_latitude = otherUser.home_latitude,
				other_longitude = otherUser.home_longitude, 
        			distance = euclidian_distance
			)
			if euclidian_distance==0:
				pass
			else:
				output.append(json_obj)
		#print(otherUser.home_latitude)
		output_sorted = sorted(output, key=lambda k: k['distance'])
		best_match_dist_obj = output_sorted[0]
		next_best_match_dist_obj = output_sorted[1]
		best_match_email = best_match_dist_obj["other_email"]
		next_best_match_email = next_best_match_dist_obj["other_email"]
		#best_match_org_obj=queryset.get(email=best_match_email)
		
		best_match = thequeryset.filter(email=best_match_email)
		next_best_match = thequeryset.filter(email=next_best_match_email)
		#best_matches = best_match | next_best_match #merging querysets
		best_matches = list(best_match) + list(next_best_match)
		#best_matches = thequeryset.filter(email__in=[best_match_email,next_best_match_email])
		
		serializer = UserSerializer(best_matches, many=True)
		
		#serializer = DistanceSerializer(output_sorted,many=True)
		
		#return super(DistanceView, self).retrieve(request,*args,**kwargs)
		#return Response(serializer.data)
		
		#return Response({'best_match':best_match["other_email"]})
		return Response(serializer.data)
		#return Response({'initial_latitude': initial_latitude, 'initial_longitude': initial_longitude})

   # @detail_route()
    #def date_list(self, request, pk=None):
     #   user = self.get_object() # retrieve an object by pk provided
      #  isSearchingUsers = Users.objects.filter(is_searching=True).distinct()
       # schedule_json = UserSerializer(isSearchingUsers, many=True)
        #return (Response(schedule_json.data))


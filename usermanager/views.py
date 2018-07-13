from django.shortcuts import render
from rest_framework import generics
from .serializers import UsersSerializer
from .models import Users
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

@method_decorator(csrf_exempt, name='dispatch')
class CreateView(generics.ListCreateAPIView):
	queryset = Users.objects.all()
	serializer_class = UsersSerializer
	@csrf_exempt
	def perform_create(self, serializer):
		serializer.save()
	#@csrf_exempt
	#def post(self. request, *args, **kwargs):
   		#return self.get(request, *args, **kwargs)

# Create your views here.
@csrf_exempt
def post_list(request):
    return render(request, 'usermanager/post_list.html', {})


class DistanceView(CreateView):
	model = Users

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Users
from .serializers import UsersSerializer

# Create your tests here.

class BaseViewTest(APITestCase):
	client = APIClient()

	@staticmethod
	def create_song(id="", first_name=""):
		if id!="" and first_name!="":
			Users.objects.create(id=id, first_name=first_name)

	def setUp(self):
        	self.create_song("like glue", "sean paul")
        	self.create_song("simple song", "konshens")
      	  	self.create_song("love is wicked", "brick and lace")
        	self.create_song("jam rock", "damien marley")


class GetAllSongsTest(BaseViewTest):

    def test_get_all_songs(self):
        """
        This test ensures that all songs added in the setUp method
        exist when we make a GET request to the songs/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("songs-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = Users.objects.all()
        serialized = UsersSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


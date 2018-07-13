

"""unicab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
#from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from unicab.viewsets import UserViewSet
from unicab.viewsets import UserInDatabase
from unicab.viewsets import DistanceView
#from .views import CreateView

#MAIN AOU URL ROOT
router = routers.DefaultRouter()

#Register a route to the router
router.register(r'users', UserViewSet, 'Users')
router.register(r'userInDatabase',UserInDatabase, 'UserInDatabase')
#router.register(r'distanceview', DistanceView, 'DistanceView')
distance_view = DistanceView.as_view({'get':'retrieve'})

urlpatterns = [
    	path('admin/', admin.site.urls),
	path('api/', include(router.urls)),
	path(r'distanceview/<email>/', distance_view),

	#path(r'^bucketlists/$', CreateView.as_view(), name="create"),
	path('', include('usermanager.urls'))
]


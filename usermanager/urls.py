#urls go here
from django.conf.urls import *
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView

urlpatterns = [
      url(r'^$', views.post_list, name='post_list'),
      #url(r'^bucketlists/$', CreateView.as_view(), name="create"),
]


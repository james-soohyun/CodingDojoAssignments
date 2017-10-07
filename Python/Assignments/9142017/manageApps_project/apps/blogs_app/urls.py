
from django.conf.urls import url
from . import views

def test(request):
	print "It's working!"

urlpatterns = [
    url(r'^$', views.index),
    url(r'^new/', views.new),
    url(r'^create/', views.create),
    url(r'^15/$', views.show),
    url(r'^15/edit/$', views.edit),
    url(r'^15/delete$', views.delete),
]

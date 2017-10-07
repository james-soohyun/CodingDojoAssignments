
from django.conf.urls import url
from . import views

def test(request):
	print "It's working!"

urlpatterns = [
    url(r'^users/$', views.index),
    url(r'^register/$', views.register),
    url(r'^login/$', views.login),
    url(r'^users/new/$', views.register),
]

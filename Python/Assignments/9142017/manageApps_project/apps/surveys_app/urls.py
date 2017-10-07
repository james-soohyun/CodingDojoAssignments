
from django.conf.urls import url
from . import views

def test(request):
	print "It's working!"

urlpatterns = [
    url(r'^$', views.index),
    url(r'^new/', views.new),
]

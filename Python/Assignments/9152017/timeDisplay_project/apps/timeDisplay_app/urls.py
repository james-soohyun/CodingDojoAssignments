
from django.conf.urls import url, include
from . import views

def test(request):
	print "It's working!! IOAD:OJIO:AJ:JF"

urlpatterns = [
    url(r'^$', views.index),

]

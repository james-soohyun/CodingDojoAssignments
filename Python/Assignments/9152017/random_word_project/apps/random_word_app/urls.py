from django.conf.urls import url, include
from . import views

def test(request):
	print "YOU'LL FLOAT TOO!\n"


urlpatterns = [
    url(r'^$', views.index),
    url(r'^generate$', views.generate)
]

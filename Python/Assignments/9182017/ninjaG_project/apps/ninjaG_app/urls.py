
from django.conf.urls import url, include
from . import views
from django.http import HttpResponse


def test(request):
	return HttpResponse('This is app level')


urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^reset$', views.reset)
]

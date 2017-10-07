
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^display', views.display),
    url(r'^reset', views.reset)
]

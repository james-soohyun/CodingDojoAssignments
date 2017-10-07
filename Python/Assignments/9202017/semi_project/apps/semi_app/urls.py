from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^users$', views.index),
    url(r'^users/new$', views.add),
    url(r'^users/create', views.create),
    url(r'^users/delete', views.delete),
]

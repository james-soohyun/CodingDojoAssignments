
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^register$', views.register),
    url(r'^create$', views.create),
    url(r'^login$', views.loginPage),
    url(r'^loginVal$', views.login),
    url(r'^dashboard$', views.dashboard),
]

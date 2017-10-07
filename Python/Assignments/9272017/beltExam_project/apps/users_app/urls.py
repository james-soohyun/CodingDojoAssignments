
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^friends/$', views.dashboard),
    url(r'^logout/$', views.logout),
    url(r'^user/(?P<user_id>\d+)$', views.display),
    url(r'^addFriend/(?P<user_id>\d+)$', views.addFriend),
    url(r'^removeFriend/(?P<user_id>\d+)$', views.removeFriend),
]

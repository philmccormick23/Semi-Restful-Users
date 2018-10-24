from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^users/(?P<id>\d+)$', views.user, name='show'),
    url(r'^users/new$', views.new),
    url(r'^process$', views.process),
    url(r'^(?P<id>\d+)/update$', views.update, name='update'),
    url(r'^(?P<id>\d+)/tag$', views.tag, name='tag'),
    url(r'^users/(?P<id>\d+)/edit$', views.edit, name='edit'),
    url(r'^users/(?P<id>\d+)/delete$', views.delete, name='delete'),
]   
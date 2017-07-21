from django.conf.urls import url
from .import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^qprocess$', views.q_process, name='q_process'),
    url(r'^favorites/(?P<id>\d+)$', views.favorites, name='favorites'),
    url(r'^users/(?P<id>\d+)$', views.users, name='users'),
    url(r'^remove/(?P<id>\d+)$', views.remove, name='remove'),
]

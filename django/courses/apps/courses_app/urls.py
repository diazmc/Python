from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.create),
    url(r'^courses/destroy/(?P<id>\d+)$', views.destroy),
    url(r'^(?P<id>\d+)$', views.delete)
]
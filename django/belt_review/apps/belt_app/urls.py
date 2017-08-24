from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^login$', views.login),
    url(r'^books$', views.books),
    url(r'^books/add$', views.addbookspage),
    url(r'^addbook$', views.addbook),
    url(r'^logout$', views.logout),
    url(r'^users/(?P<id>\d+)$', views.displayUser),
    url(r'^books/(?P<id>\d+)$', views.displayBook)
]
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^projects$', views.projects),
    url(r'^about$', views.aboutme),
    url(r'^testimonials$', views.testimonials)
]
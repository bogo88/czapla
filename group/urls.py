from django.conf.urls import patterns, include, url
from group import views

urlpatterns = patterns('',
                       url(r'^(?P<group_id>[0-9]+)',views.details, name='details'))
from django.conf.urls import patterns, include, url
from meal import views

urlpatterns = patterns('',
                       url(r'^restaurant/group/(?P<group_id>[0-9]+)',views.restaurant, name='restaurant'),
                       url(r'^select/(?P<order_id>[0-9]+)',views.select, name='select'))
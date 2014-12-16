from django.conf.urls import patterns, include, url
from item import views

urlpatterns = patterns('',
                       #url(r'^$',views.index, name='index'),
                       url(r'^add/(?P<order_id>[0-9]+)/meal/(?P<meal_id>[0-9]+)',views.add, name='add'))
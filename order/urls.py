from django.conf.urls import patterns, include, url
from order import views

urlpatterns = patterns('',
                       url(r'^add',views.add, name='add'),
                       url(r'^(?P<order_id>[0-9]+)',views.details, name='details'))
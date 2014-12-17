from django.conf.urls import patterns, include, url
from profile import views

urlpatterns = patterns('',
                       url(r'^$',views.index, name='index'),
                       url(r'^register',views.register, name='register'),
                       )
from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()
urlpatterns = patterns('',
                       url(r'^', include('home.urls', namespace='home')),
                       url(r'^profile/', include('profile.urls', namespace='profile')),
                       url(r'^group/', include('group.urls', namespace='group')),
                       url(r'^item/', include('item.urls', namespace='item')),
                       url(r'^order/', include('order.urls', namespace='order')),
                       url(r'^meal/', include('meal.urls', namespace='meal')),
                       url(r'^admin/', include(admin.site.urls)),)

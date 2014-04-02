from django.conf.urls import patterns, url

from waterpoints import views

urlpatterns = patterns('',
	url(r'^(?P<user_id>\d+)/$', views.waterpointDetail, name = 'waterpointDetail'),
    url(r'^imagesupload/(?P<user_id>\d+)/$', views.waterpointPhotos, name = 'waterpointPhotos'),
    url(r'^(?P<user_id>\d+)/(?P<user_location>\S+)/$', views.update_waterpoint, name = 'update_waterpoint'),
    
)

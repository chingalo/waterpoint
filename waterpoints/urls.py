from django.conf.urls import patterns, url

from waterpoints import views

urlpatterns = patterns('',
	url(r'^(?P<user_id>\d+)/$', views.waterpointDetail, name = 'waterpointDetail'),
    url(r'^imagesupload/(?P<user_id>\d+)/$', views.waterpointPhotos, name = 'waterpointPhotos'),
    url(r'^(?P<user_id>\d+)/(?P<user_location>\S+)/$', views.update_waterpoint, name = 'update_waterpoint'),
    url(r'^waterConnectionSummaryEngineer/(?P<user_id>\d+)/$', views.water_connection_summary_engineer, name='water_connection_summary_engineer'),
    url(r'^waterConnectionSummaryAdmin/(?P<user_id>\d+)/$', views.water_connection_summary_admin, name='water_connection_summary_admin'),
    url(r'^waterConnectionDetailsEngineer/(?P<user_id>\d+)/(?P<water_connection_id>\d+)/$', views.water_connection_DetailsFromEngineer, name='water_connection_details_from_engineer'),
)

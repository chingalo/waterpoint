from django.conf.urls import patterns, url

from users import views

urlpatterns = patterns('',
    url(r'^$', views.authorize, name='authorize'),
    url(r'^(?P<user_id>\d+)/createEngineer/$', views.createEngineer, name='createEngineer'),
    url(r'^(?P<user_id>\d+)/createChairperson/$', views.createChairperson, name='createChairperson'),
    url(r'^(?P<user_id>\d+)/adminHome/$', views.adminHome, name='adminhome'),
    url(r'^(?P<user_id>\d+)/enginerHome/$', views.enginerHome, name='engineerhome'),
    url(r'^(?P<user_id>\d+)/(?P<user_e_mail>\S+)/(?P<user_password>\S+)/(?P<user_position>\S+)/logout/$', views.log_out, name='log_out'),
    url(r'^reportSummaryEngineer/(?P<user_id>\d+)/$', views.report_summary_engineer, name='report_summary_engineer'),
    url(r'^cowsoSummaryEngineer/(?P<user_id>\d+)/$', views.cowso_summary_engineer, name='cowso_summary_engineer'),
    url(r'^cowsoSummaryAdmin/(?P<user_id>\d+)/$', views.cowso_summary_Admin, name='cowso_summary_admin'),
    url(r'^engineerSummaryAdmin/(?P<user_id>\d+)/$', views.engineer_summary_Admin, name='engineer_summary_admin'),
    url(r'^cowsoDetailsEngineer/(?P<user_id>\d+)/(?P<cowso_id>\d+)/$', views.cowso_DetailsFromEngineer, name='cowso_details_from_engineer'),
    url(r'^cowsoDetailsAdmin/(?P<user_id>\d+)/(?P<cowso_id>\d+)/$', views.cowso_DetailsFromAdmin, name='cowso_details_from_admin'),
    url(r'^cowsoDetails/(?P<user_id>\d+)/(?P<engineer_id>\d+)/$', views.engineer_DetailsFromAdmin, name='engineer_details_from_admin'),
   
)

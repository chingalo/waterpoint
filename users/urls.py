from django.conf.urls import patterns, url

from users import views

urlpatterns = patterns('',
    url(r'^$', views.authorize, name='authorize'),
    url(r'^(?P<user_id>\d+)/createEngineer/$', views.createEngineer, name='createEngineer'),
    url(r'^(?P<user_id>\d+)/createChairperson/$', views.createChairperson, name='createChairperson'),
    url(r'^(?P<user_id>\d+)/adminHome/$', views.adminHome, name='adminhome'),
    
   
)

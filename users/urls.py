from django.conf.urls import patterns, url

from users import views

urlpatterns = patterns('',
    url(r'^$', views.authorize, name='authorize'),
    url(r'^createEngineer/$', views.createEngineer, name='createEngineer'),
    url(r'^createChairperson/$', views.createChairperson, name='createChairperson'),
   
)

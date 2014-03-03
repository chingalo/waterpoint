from django.conf.urls import patterns, url

from users import views

urlpatterns = patterns('',
    url(r'^$', views.authorize, name='authorize'),
    url(r'^$', views.createEngineer, name='createEngineer'),
    url(r'^$', views.createChairperson, name='createChairperson'),
   
)

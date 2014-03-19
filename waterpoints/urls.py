from django.conf.urls import patterns, url

from waterpoints import views

urlpatterns = patterns('',
    url(r'^$', views.waterpointDetail, name = 'waterpointDetail'),
)

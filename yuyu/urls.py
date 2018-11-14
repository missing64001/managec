from django.conf.urls import url
from .views import *
from django.contrib import admin

urlpatterns = [
    # url(r'^$', index, name='index'),
    # url(r'^p/(?P<article_id>[0-9]+)/$', detail,name='detail'),

    url(r'^$',Index, name='index'),
    url(r'^opt_timer/$',OptTimer, name='OptTimer'),


]
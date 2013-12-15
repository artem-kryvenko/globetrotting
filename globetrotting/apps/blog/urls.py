# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url


urlpatterns = patterns('blog.views',
    url(r'^$', 'home', name='home'),
    url(r'^archive/$', 'archive', name='archive'),
	url(r'^archive/(?P<post_id>\d+)/$', 'post_detail', name='detail'),

)
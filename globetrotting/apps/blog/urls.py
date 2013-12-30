# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = patterns('blog.views',
    url(r'^$', 'home', name='home'),
    url(r'^archive/$', 'archive', name='archive'),
	url(r'^archive/(?P<post_id>\d+)/$', 'post_detail', name='detail'),


) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'globetrotting.views.home', name='home'),
    # url(r'^globetrotting/', include('globetrotting.foo.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

	url(r'^blog/', include('blog.urls'))
)

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'members.views.home', name='home'),
    url(r'^islemler/', include('accounting.urls')),
    url(r'^uyelik/', include('members.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('allauth.urls')),
)

urlpatterns += staticfiles_urlpatterns()

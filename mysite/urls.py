"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', 'mysite.views.hello'),
    url(r'^form/$', 'mysite.views.url'),
    url(r'^time/$', 'mysite.views.date_time'),
    url(r'^time/plus/(\d)/$', 'mysite.views.hours_ahead'),
	url(r'^index/$', 'mysite.views.index_artist'),
    url(r'^khoj/$', 'album.views.khoj_form'),
    url(r'^khoj_result/$', 'album.views.khoj_result'),
    url(r'^album_list/$', 'album.views.album_list'),
    url(r'^album/(?P<username>[\w|\W]+)/$', 'album.views.album_go'),
    url(r'^gitikar/(?P<username>[\w|\W]+)/$', 'album.views.git_go'),
    url(r'^prokashok/(?P<username>[\w|\W]+)/$', 'album.views.pro_go'),
    url(r'^shilpi/(?P<username>[\w|\W]+)/$', 'album.views.shi_go'),
    url(r'^band/(?P<username>[\w|\W]+)/$', 'album.views.ban_go'),
    url(r'^gaan/(?P<username>[\w|\W]+)/$', 'album.views.gaa_go'),
    url(r'^list/[\w|\W]+/album_list/(?P<username>[\w|\W]+)/$', 'album.views.album_go'),
    url(r'^newlist/$', 'album.views.newlist'),
    url(r'^list/$', 'album.views.comb_list'),
    url(r'^$', 'album.views.comb_list'),
    url(r'^newlist/$', 'album.views.newlist'),
    url(r'^(?P<alf>[\w|\W]+)/$', 'album.views.alf_list', name='alphabet_list'),
    url(r'^contact/$', 'mysite.views.contact'),
)

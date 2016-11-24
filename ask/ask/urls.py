from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('qa.views',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'test'), 
    url(r'^login/.*$', 'test', name='login'), 
    url(r'^signup/.*', 'test', name='signup'), 
    url(r'^question/(?P<id>[0-9]+)/$', 'question', name='question'), 
    url(r'^ask/.*', 'test', name='ask'), 
    url(r'^popular/.*', 'list_popular', name='popular'), 
    url(r'^new/.*', 'list_new', name='new'), 
)

from django.conf.urls import patterns, include, url
from django.contrib.auth import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),
)

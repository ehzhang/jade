from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url


urlpatterns = patterns('jade.apps.common.views',
    url(r'^$', 'home', name='home'),
    url(r'^card/$', 'card'),
)

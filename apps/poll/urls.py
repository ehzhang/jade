from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url


urlpatterns = patterns('jade.apps.poll.views',
    url(r'^(?P<poll_id>\d+)/$', 'poll_atomic', name='poll_atomic'),
)

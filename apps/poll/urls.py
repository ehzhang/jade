from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url


urlpatterns = patterns('jade.apps.poll.views',
    url(r'^(?P<poll_id>\d+)/$', 'poll_atomic', name='poll_atomic'),
    url(r'^card/(?P<card_id>\d+)/$', 'card_atomic',
        name='card_atomic'),

    url(r'^create/$', 'create_poll', name='create_poll'),
    url(r'^poll_redraw/$', 'poll_redraw', name='poll_redraw'),

    url(r'^create_option/$', 'create_option', name='create_option'),
    url(r'^option_upvote/$', 'option_upvote', name='option_upvote'),
    url(r'^option_downvote/$', 'option_downvote', name='option_downvote'),
    url(r'^option_redraw/$', 'option_redraw', name='option_redraw'),

    url(r'^create_comment/$', 'create_comment',
        name='create_comment'),
    url(r'^comment_upvote/$', 'comment_upvote'),
    url(r'^comment_downvote/$', 'comment_downvote'),
)

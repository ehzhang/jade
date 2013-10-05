from json import dumps

from django.conf.settings import DEBUG
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render

from jade.apps.poll.models import Comment
from jade.apps.poll.models import Option
from jade.apps.poll.models import Poll


def JSONResponse(data):
    return HttpResponse(
        dumps(data),
        content_type='application/json'
    )

def get_post_request_attr(request, attr):
    '''
    Gets 
    '''
    if DEBUG:
        return request.REQUEST.get(attr)
    else:
        return request.POST.get(attr)

def transform_poll_id(poll_hash):
    return poll_hash


def poll_atomic(request, poll_id):
    
    poll = Poll.objects.get(id=transform_poll_id(poll_id))
    context = {
        'poll': poll,
    }

    return render(request, 'poll.html', context)


def create_poll(request):
    name = get_post_request_attr(request, 'name')
    poll = Poll.objects.create(name=name)
    poll.save()

    data = {
        'result': 'success',
        'url': reverse('poll_atomic', args=(poll.id, ))
    }
    return JSONResponse(data)

def create_option(request):
    poll_id = get_post_request_attr(request, 'poll_id')
    submitter = get_post_request_attr(request, 'submitter')
    text = get_post_request_attr(request, 'text')

    poll = Poll.objects.get(id=poll_id)
    poll 


def option_upvote(request, option_id):
    import ipdb; ipdb.set_trace()
    option = Option.objects.get(id=option_id)
    option.upvote()

    data = {
        'result': 'success',
    }
    return JSONResponse(data)

def option_downvote(request, option_id):
    pass

def comment_upvote(request, comment_id):
    pass

def comment_downvote(request, comment_id):
    pass

from json import dumps

from django.http import HttpResponse
from django.shortcuts import render

from jade.apps.poll.models import Comment
from jade.apps.poll.models import Option
from jade.apps.poll.models import Poll

def poll_atomic(request, poll_id):
    
    poll = Poll.objects.get(id=poll_id)
    context = {
        'poll': poll,
    }

    return render(request, 'poll.html', context)

def option_upvote(request, option_id):
    option = Option.objects.get(id=option_id)
    option.upvote()

    response = {
        'result': 'success',
    }
    return HttpResponse(
        dumps(response),
        content_type='application/json',
    )

def option_downvote(request, option_id):
    pass

def comment_upvote(request, comment_id):
    pass

def comment_downvote(request, comment_id):
    pass

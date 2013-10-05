from json import dumps

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


def poll_atomic(request, poll_id):
    
    poll = Poll.objects.get(id=poll_id)
    context = {
        'poll': poll,
    }

    return render(request, 'poll.html', context)


def create_poll(request):
    name = request.POST.get('name') or request.GET.get('name')
    poll = Poll.objects.create(name=name)
    poll.save()

    data = {
        'result': 'success',
        'url': reverse('poll_atomic', args=(poll.id, ))
    }
    return JSONResponse(data)


def option_upvote(request, option_id):
    option = Option.objects.get(id=option_id)
    votes = request.session.get('option_votes', {})
    allowed = not (option_id in votes and votes[option_id] > 0)
    if allowed:
        option.upvote()

    if option_id in votes:
        # change vote
        votes[option_id] += 1
        option.undo_downvote()
    else:
        votes[option_id] = 1

    data = {
        'result': 'success' if allowed else 'failure',
    }
    return JSONResponse(data)

def option_downvote(request, option_id):
    option = Option.objects.get(id=option_id)
    votes = request.session.get('option_votes', {})
    allowed = not (option_id in votes and votes[option_id] < 0)
    if allowed:
        option.downvote()

    if option_id in votes:
        # change vote
        votes[option_id] -= 1
        option.undo_upvote()
    else:
        votes[option_id] = -1

    data = {
        'result': 'success' if allowed else 'failure',
    }
    return JSONResponse(data)

def comment_upvote(request, comment_id):
    comment = Comment.objects.get(id=comment)
    votes = request.session.get('comment_votes', {})
    allowed = not (comment_id in votes and votes[comment_id] > 0)
    if allowed:
        comment.upvote()

    if comment_id in votes:
        # change vote
        votes[comment_id] += 1
        comment.undo_downvote()
    else:
        votes[comment_id] = 1

    data = {
        'result': 'success' if allowed else 'failure',
    }
    return JSONResponse(data)

def comment_downvote(request, comment_id):
    comment = Comment.objects.get(id=comment)
    votes = request.session.get('comment_votes', {})
    allowed = not (comment_id in votes and votes[comment_id] < 0)
    if allowed:
        comment.downvote()

    if comment_id in votes:
        # change vote
        votes[comment_id] -= 1
        comment.undo_upvote()
    else:
        votes[comment_id] = -1

    data = {
        'result': 'success' if allowed else 'failure',
    }
    return JSONResponse(data)

from json import dumps

from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render

from jade.apps.poll.models import Comment
from jade.apps.poll.models import Option
from jade.apps.poll.models import Poll
from jade.apps.poll.utils import Card
from jade.apps.poll.utils import CardBack


def JSONResponse(data):
    return HttpResponse(
        dumps(data),
        content_type='application/json'
    )

def get_post_request_attr(request, attr):
    '''
    Gets attributes 
    '''
    if settings.DEBUG:
        return request.REQUEST.get(attr)
    else:
        return request.POST.get(attr)

def transform_poll_id(poll_hash):
    return poll_hash


def poll_atomic(request, poll_id):
    
    poll = Poll.objects.get(id=transform_poll_id(poll_id))
    cards = [Card(option.id) for option in 
             Option.objects.filter(poll=poll)]
    context = {
        'poll': poll,
        'cards': cards,
    }

    return render(request, 'poll.html', context)

def card_atomic(request, card_id):

    option = Option.objects.get(id=card_id)
    poll = option.poll
    card = CardBack(card_id)

    context = {
        'card': card,
        'poll': poll,
    }

    return render(request, 'card.html', context)


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
    # race condition bug below. fix later
    public_id = Option.objects.filter(poll=poll).count()

    option = Option.objects.create(
        poll=poll,
        public_id=public_id,
        submitter=submitter,
        text=text,
    )
    option.save()

    data = {
        'result': 'success',
    }
    return JSONResponse(data)


def create_comment(request):
    option_id = get_post_request_attr(request, 'option_id')
    submitter = get_post_request_attr(request, 'submitter')
    text = get_post_request_attr(request, 'text')

    option = Option.objects.get(id=option_id)
    # race condition bug below. fix later
    public_id = Comment.objects.filter(option=option).count()

    comment = Comment.objects.create(
        option=option,
        public_id=public_id,
        text=text,
    )
    if submitter:
        comment.submitter = submitter
    comment.save()

    data = {
        'result': 'success'
    }
    return JSONResponse(data)


def option_upvote(request):
    option_id = get_post_request_attr(request, 'option_id')
    option = Option.objects.get(id=option_id)
    votes = request.session.get('option_votes', {})

    if option_id not in votes:
        option.upvote()
        votes[option_id] = 1
    elif votes[option_id] == -1:
        option.undo_downvote()
        option.upvote()
        votes[option_id] = 1
    elif votes[option_id] == 0:
        option.upvote()
        votes[option_id] = 1
    elif votes[option_id] == 1:
        option.undo_upvote()
        votes[option_id] = 0

    request.session['option_votes'] = votes
    data = {
        'result': 'success',
    }
    return JSONResponse(data)

def option_downvote(request):
    option_id = get_post_request_attr(request, 'option_id')
    option = Option.objects.get(id=option_id)
    votes = request.session.get('option_votes', {})

    if option_id not in votes:
        option.downvote()
        votes[option_id] = -1
    elif votes[option_id] == 1:
        option.undo_upvote()
        option.downvote()
        votes[option_id] = -1
    elif votes[option_id] == 0:
        option.downvote()
        votes[option_id] = -1
    elif votes[option_id] == -1:
        option.undo_downvote()
        votes[option_id] = 0

    request.session['option_votes'] = votes
    data = {
        'result': 'success',
    }
    return JSONResponse(data)

def comment_upvote(request):
    comment_id = get_post_request_attr(request, 'comment_id')
    comment = Comment.objects.get(id=comment_id)
    votes = request.session.get('comment_votes', {})

    if comment_id not in votes:
        comment.upvote()
        votes[comment_id] = 1
    elif votes[comment_id] == -1:
        comment.undo_downvote()
        comment.upvote()
        votes[comment_id] = 1
    elif votes[comment_id] == 0:
        comment.upvote()
        votes[comment_id] = 1
    elif votes[comment_id] == 1:
        comment.undo_upvote()
        votes[comment_id] = 0

    request.session['comment_votes'] = votes
    data = {
        'result': 'success',
    }
    return JSONResponse(data)

def comment_downvote(request):
    comment_id = get_post_request_attr(request, 'comment_id')
    comment = Comment.objects.get(id=comment_id)
    votes = request.session.get('comment_votes', {})

    if comment_id not in votes:
        comment.downvote()
        votes[comment_id] = -1
    elif votes[comment_id] == 1:
        comment.undo_upvote()
        comment.downvote()
        votes[comment_id] = -1
    elif votes[comment_id] == 0:
        comment.downvote()
        votes[comment_id] = -1
    elif votes[comment_id] == -1:
        comment.undo_downvote()
        votes[comment_id] = 0

    request.session['comment_votes'] = votes
    data = {
        'result': 'success',
    }
    return JSONResponse(data)

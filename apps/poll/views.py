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

from django.shortcuts import render

from jade.apps.poll.models import Option
from jade.apps.poll.utils import Card


def home(request):
    return render(request, 'index.html')


def card(request):
    card = Card(Option.objects.all()[1].id)
    context = {
        'card': card,
    }
    return render(request, 'card.html', context)


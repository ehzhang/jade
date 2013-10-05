from django.http import HttpResponse
# Create your views here.

def poll_atomic(request, poll_id):
    return HttpResponse(poll_id)


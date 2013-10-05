from django.contrib import admin

from jade.apps.poll.models import Comment
from jade.apps.poll.models import Option
from jade.apps.poll.models import Poll


admin.site.register(Comment)
admin.site.register(Option)
admin.site.register(Poll)


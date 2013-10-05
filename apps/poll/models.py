from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Poll(models.Model):

    name = models.CharField(
        _('poll name'),
        max_length=200,
    )

    timestamp = models.TimeField(
        _('poll create time'),
        auto_now_add=True,
    )

    def __unicode__(self):
        return u'%s' % (self.name, )


class Option(models.Model):

    poll = models.ForeignKey(Poll)

    public_id = models.IntegerField(
        _('public option id'),
    )

    submitter = models.CharField(
        _('name of option submitter'),
        max_length=100,
    )

    text = models.CharField(
        _('option description'),
        max_length=200,
    )

    timestamp = models.TimeField(
        _('option create time'),
        auto_now_add=True
    )

    upvotes = models.IntegerField(
        _('number of upvotes'),
    )

    def __unicode__(self):
        return u'%s' % (self.text, )

    downvotes = models.IntegerField(
        _('number of downvotes'),
    )

class Comment(models.Model):

    option = models.ForeignKey('Option')

    public_id = models.IntegerField(
        _('public comment id'),
    )

    submitter = models.CharField(
        _('name of comment submitter'),
        max_length=100,
    )

    timestamp = models.TimeField(
        _('comment create time'),
        auto_now_add=True,
    )

    text = models.TextField(
        _('comment text'),
    )

    upvotes = models.IntegerField(
        _('number of upvotes'),
    )

    downvotes = models.IntegerField(
        _('number of downvotes'),
    )

    def __unicode__(self):
        return u'%s' % (self.text, )


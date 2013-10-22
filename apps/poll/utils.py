from jade.apps.poll.models import Comment
from jade.apps.poll.models import Option


class Card(object):
    option_id = None
    text = None
    submitter = None
    votes = None
    comments = None
    user_vote = None

    def __init__(self, option_id, request = None):
        self.option_id = option_id
        option = Option.objects.get(id=option_id)

        self.text = option.text
        self.submitter = option.submitter
        self.votes = option.votes
        self.comments = [
            DisplayComment(comment) for comment in
            Comment.objects.filter(option=option)
        ]

        if request and 'option_votes' in request.session and \
            unicode(option_id) in request.session['option_votes']:
            self.user_vote = request.session['option_votes'][unicode(option_id)]
        else:
            self.user_vote = 0

    def to_json(self):
        data = {
            'option_id': self.option_id,
            'submitter': self.submitter,
            'text': self.text,
            'user_vote': self.user_vote,
            'votes': self.votes,
            'comments': self.comments,
        }
        return data




class DisplayComment(object):
    comment_id = None
    text = None
    submitter = None
    votes = None
    
    def __init__(self, comment):
        self.comment_id = comment.id
        self.text = comment.text
        self.submitter = comment.submitter
        self.votes = comment.votes()


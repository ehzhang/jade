from jade.apps.poll.models import Comment
from jade.apps.poll.models import Option


class Card(object):
    option_id = None
    text = None
    submitter = None
    votes = None
    comments = None

    def __init__(self, option_id):
        self.option_id = option_id
        option = Option.objects.get(id=option_id)

        self.text = option.text
        self.submitter = option.submitter
        self.votes = option.votes()
        self.comments = [
            DisplayComment(comment) for comment in
            Comment.objects.filter(option=option)
        ]


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


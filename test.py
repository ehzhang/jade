from os.path import dirname, join

print join(dirname(__file__), '/templates')
print dirname(__file__)
print __file__

import ipdb; ipdb.set_trace()

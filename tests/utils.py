#!/usr/bin/env python
import random
import string

# Python3 compatibility code
try:
    range = xrange
except NameError:
    pass


def random_string(n):
    chars = (string.ascii_letters + string.digits + string.punctuation)
    msg = ''.join(random.choice(chars) for x in range(n))
    return msg

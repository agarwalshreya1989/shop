import string
import random
from django.contrib.sites.models import Site


def generate_random_string(length, stringset=string.ascii_letters+string.digits):
    '''
    Returns a string with `length` characters chosen from `stringset`
    >>> len(generate_random_string(20)) == 20
    '''
    return ''.join([random.choice(stringset) for n in range(length)])


def get_current_site():
    return Site.objects.get_current()

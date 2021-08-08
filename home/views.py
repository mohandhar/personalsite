import logging

from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from .models import Person

logger = logging.getLogger(__name__)


def index(request):
    """Home page of the website"""
    person = get_object_or_404(
        Person.objects,
        first_name='Mohan',
        last_name='Dhar',
    )
    logger.info('Person: ', person)
    context = dict(
        person=person
    )
    return render(request, 'home/index.html', context)

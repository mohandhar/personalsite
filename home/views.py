import logging

from django.db.models import Q
from django.shortcuts import get_object_or_404, get_list_or_404, render

from .models import Person, Experience, Accomplishment, Education

logger = logging.getLogger(__name__)


def index(request):
    """Home page of the website"""
    person = get_object_or_404(
        Person.objects,
        first_name='Mohan',
        last_name='Dhar',
    )

    context = dict(
        person=person,
    )
    return render(request, 'home/index.html', context)

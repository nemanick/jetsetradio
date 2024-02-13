from django.db.models import Q
from django.contrib.auth import get_user_model

User = get_user_model()


def search(reqeust):
    '''Search function view'''
    search_query = ''

    if reqeust.GET.get('query'):
        search_query = reqeust.GET.get('query')

    artist = User.objects.distinct().filter(
        Q(username__icontains=search_query)
    )

    return artist

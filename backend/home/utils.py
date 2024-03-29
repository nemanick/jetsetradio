from django.db.models import Q
from django.contrib.auth import get_user_model
from music.models import Music
from genre.models import Genre

User = get_user_model()


def search(reqeust):
    '''Search function view (music, albums, artists and genres)'''
    search_query = ''

    if reqeust.GET.get('query'):
        search_query = reqeust.GET.get('query')

    only_published_music = Music.objects.filter(published=True)

    music = only_published_music.distinct().filter(
        Q(title__icontains=search_query) |
        Q(lyrics__icontains=search_query)
    )
    artist = User.objects.distinct().filter(
        Q(username__icontains=search_query)
    )
    genre = Genre.objects.distinct().filter(
        Q(title__icontains=search_query)
    )

    return music, artist, genre

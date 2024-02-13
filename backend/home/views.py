from django.shortcuts import render
from django.contrib.auth import get_user_model
from genre.models import Genre
from music.models import Music
from home.models import HomePagePoster as Poster
from home.utils import search

User = get_user_model()

ALL_MAX_COUNT = 12
SONGS_MAX_COUNT = 5


def homePage(request):
    '''Home page view'''
    posters = Poster.objects.all()
    new_song_for_player = Music.objects.filter(
        published=True).order_by('-created').first()
    get_genres = Genre.objects.all()
    get_songs = Music.objects.filter(
        published=True).order_by('-created')[:SONGS_MAX_COUNT]
    get_single_songs = Music.objects.filter(
        published=True).order_by(
            '-created')[:SONGS_MAX_COUNT]
    get_top_songs = Music.objects.filter(
        published=True).order_by('-page_view')[:SONGS_MAX_COUNT]
    get_artists = User.objects.all().order_by('-created')[:ALL_MAX_COUNT]

    context = {
        'genres': get_genres,
        'artists': get_artists,
        'songs': get_songs,
        'singles': get_single_songs,
        'top_songs': get_top_songs,
        'player': new_song_for_player,
        'posters': posters
    }
    return render(request, 'home/home.html', context)


def searchPage(request):
    '''Search page view'''
    music, artist, genre = search(request)
    context = {
        'songs': music[:ALL_MAX_COUNT],
        'artists': artist[:ALL_MAX_COUNT],
        'genres': genre[:ALL_MAX_COUNT],
        'query': request.GET.get('query')
    }

    return render(request, 'home/search.html', context)

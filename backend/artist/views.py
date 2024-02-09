from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserEditFrom

from album.models import Album
from genre.models import Genre
from music.models import Music
from artist.utils import search

User = get_user_model()


def artistsPage(request):
    get_artists = search(request)
    get_genres = Genre.objects.all()
    new_song_for_player = Music.objects.filter(
        published=True).order_by('-created').first()
    context = {
        'artists': get_artists,
        'genres': get_genres,
        'player': new_song_for_player
    }

    return render(request, 'artist/artists.html', context)


def signleArtistPage(request, pk, slug):
    get_artist = User.objects.get(id=pk, slug=slug)
    print(get_artist.picture)
    get_artist_albums = Album.objects.filter(artists=get_artist)
    new_song_for_player = Music.objects.filter(
        published=True).order_by('-created').first()
    context = {
        'artist': get_artist,
        'albums': get_artist_albums,
        'player': new_song_for_player
    }

    return render(request, 'artist/single-artist.html', context)


@login_required
def singleArtistEdit(request, slug, pk):
    user = User.objects.get(username=request.user.username)
    form = CustomUserEditFrom(request.POST or None, files=request.FILES or None,
                              instance=request.user)

    if request.method == 'POST':
        if form.is_valid():
            try:
                form.instance.user = request.user
                form.save()
                return redirect('single-artist', slug=user.slug, pk=user.id)
            except:
                messages.error(request, 'An error has occurred during registration')

        else:
            messages.error(request, 'An error has occurred during registration')

    context = {
        'form': form,
        'artist': user,
    }
    
    return render(request, 'artist/single-artis-edit.html', context)
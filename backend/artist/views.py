from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserEditFrom

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
    songs = Music.objects.filter(artist=get_artist,
                                 published=True).order_by('-created')
    new_song_for_player = Music.objects.filter(
        published=True).order_by('-created').first()
    context = {
        'artist': get_artist,
        'player': new_song_for_player,
        'songs': songs,
    }

    return render(request, 'artist/single-artist.html', context)


@login_required
def singleArtistEdit(request, slug, pk):
    user = request.user
    form = CustomUserEditFrom(request.POST or None,
                              files=request.FILES or None,
                              instance=user)

    if request.POST:
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Changes saved successfully.')
                return redirect('single-artist', slug=user.slug, pk=user.id)
            except Exception as e:
                messages.error(request, ('An error occurred during'
                                         f' registration: {e}'))
        else:
            messages.error(request, ('Form is not valid. Please correct the '
                                     'errors.'))

    context = {
        'form': form,
        'artist': user,
    }

    return render(request, 'artist/single-artis-edit.html', context)

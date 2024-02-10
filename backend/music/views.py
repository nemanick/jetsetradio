import os
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import FileResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404
from music.models import Music
from album.models import Album
from music.forms import MusicCommentForm
from music.utils import search


def songsPage(request):
    '''Songs page view'''
    songs = search(request)
    new_song_for_player = Music.objects.filter(
        published=True).order_by('-created').first()
    context = {'songs': songs, 'player': new_song_for_player}

    return render(request, 'music/songs.html', context)


def singleSongPage(request, slug, pk):
    '''Single song page view'''
    song = Music.objects.get(slug=slug, pk=pk)
    form = MusicCommentForm()

    if request.method == 'POST':
        form = MusicCommentForm(request.POST)
        if form.is_valid():
            """
            reply_obj = None
            try:
                reply_id = int(request.POST.get('reply_id'))
            except:
                reply_id = None

            if reply_id:
                reply_obj = MusicComment.objects.get(id=reply_id)

            if reply_obj:
                comment = form.save(commit=False)
                comment.music = song
                comment.owner = request.user
                comment.reply = reply_obj
                comment.save()"""

            comment = form.save(commit=False)
            comment.music = song
            comment.owner = request.user
            comment.active = True
            comment.save()

            messages.success(request, 'Successfully Submitted.')
            return redirect('single-song', slug=song.slug, pk=song.id)

    artist_albums = Album.objects.filter(artists=song.artists.first())[:6]
    music_comments_count = song.musiccomment_set.filter(active=True).count()
    context = {
        'song': song,
        'player': song,
        'artist_albums': artist_albums,
        'form': form,
        'comments_count': music_comments_count
    }
    return render(request, 'music/single-song.html', context)


def download_track(request, track_id):
    track = get_object_or_404(Music, id=track_id)
    track_path = track.song.path

    if os.path.exists(track_path):
        return FileResponse(open(track_path, 'rb'), as_attachment=True)
    else:
        return HttpResponseNotFound('Track not found')

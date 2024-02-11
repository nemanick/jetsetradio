import os
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import FileResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from music.models import Music
from music.forms import MusicCommentForm, MusicCreateForm
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
    song.page_view += 1
    song.save()
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

    music_comments_count = song.musiccomment_set.filter(active=True).count()
    print(song.artist.username)
    context = {
        'song': song,
        'player': song,
        'form': form,
        'comments_count': music_comments_count
    }
    return render(request, 'music/single-song.html', context)


def downloadTrack(request, track_id):
    track = get_object_or_404(Music, id=track_id)
    track_path = track.song.path

    if os.path.exists(track_path):
        return FileResponse(open(track_path, 'rb'), as_attachment=True)
    else:
        return HttpResponseNotFound('Track not found')


@login_required
def songCreateAndEdit(request, slug=None, pk=None):
    user = request.user
    is_edit = False
    instance_song = None

    if pk is not None:
        instance_song = get_object_or_404(Music, slug=slug, pk=pk)
        is_edit = True
        print(f'first {slug}')

    form = MusicCreateForm(request.POST or None,
                           files=request.FILES or None,
                           instance=instance_song)

    if request.method == 'POST':
        if form.is_valid():
            try:
                song = form.save(commit=False)
                if not is_edit:
                    song.slug = (song.title + str(user.id) +
                                 str(Music.objects.all().count() + 1))
                    song.published = True
                    song.artist = user
                song.save()
                form.save_m2m()
                return redirect('single-song', slug=song.slug, pk=song.pk)
            except Exception as e:
                messages.error(request, (f'An error '
                                         f'occurred during registration: {e}'))
        else:
            messages.error(request, ('Form is not valid. '
                                     'Please correct the errors.'))

    context = {
        'form': form,
        'is_edit': is_edit,
        'song': instance_song,
    }
    return render(request, 'music/song-create.html', context)

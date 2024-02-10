from django.db import models
from django.contrib.auth import get_user_model
from users.models import Comment
from genre.models import Genre
from album.models import Album

User = get_user_model()


class Music(models.Model):
    '''Music model'''
    title = models.CharField(max_length=220)
    thumbnail = models.ImageField(upload_to='SongsThumbnails/',
                                  default='SongsThumbnails/default.jpg')
    artists = models.ManyToManyField(User)
    album = models.ForeignKey(Album, on_delete=models.SET_NULL, null=True,
                              blank=True)
    genres = models.ManyToManyField(Genre)
    song = models.FileField(upload_to='Songs/', null=True, blank=True)
    song_duration = models.CharField(max_length=200, null=True, blank=True)
    lyrics = models.TextField(null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    published = models.BooleanField(default=False)
    page_view = models.IntegerField(default=0)
    single_track = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Music'
        verbose_name_plural = 'Music'

    def get_album_name(self):
        '''If the music object is connected to a album then get album name'''
        if self.album:
            return self.album.title
        else:
            return "No Album"

    def __str__(self):
        return self.title


class MusicComment(Comment):
    '''Music comment model'''
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    music = models.ForeignKey(Music, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Commnets'

    def comment_title(self):
        return (f'Comment on {self.music} by '
                f'{(self.owner.username if self.owner.username
                    else self.owner.email)}')

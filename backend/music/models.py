from django.db import models
from django.contrib.auth import get_user_model
from users.models import Comment
from genre.models import Genre

User = get_user_model()


class Music(models.Model):
    '''Music model'''
    title = models.CharField(max_length=256)
    thumbnail = models.ImageField(upload_to='SongsThumbnails/',
                                  default='SongsThumbnails/default.jpg')
    artist = models.ForeignKey(User, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre)
    song = models.FileField(upload_to='Songs/')
    song_duration = models.CharField(max_length=200, null=True, blank=True)
    lyrics = models.TextField(null=True)
    slug = models.SlugField(null=True, blank=True)
    published = models.BooleanField(default=False)
    page_view = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Music'
        verbose_name_plural = 'Music'

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

from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator

User = get_user_model()


class Genre(models.Model):
    name = models.CharField(max_length=150, unique=True)
    color = models.CharField('Цвет', max_length=7, unique=True,
                             validators=[
                                 RegexValidator(
                                     regex=('^#([A-Fa-f0-9]{6}|'
                                            '[A-Fa-f0-9]{3})$'),
                                     message='Ошибка в HEX коде цвета',
                                 )
                             ])
    slug = models.SlugField(max_length=200, unique=True,
                            validators=[
                                RegexValidator(
                                    regex='^[-a-zA-Z0-9_]+$',
                                    message='Ошибка в вводе slug поля',
                                )
                            ])
    
    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self) -> str:
        return self.name


class Track(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tracks',)
    title = models.CharField(max_length=256,)
    image = models.ImageField(upload_to='track_image/',)
    text = models.CharField(max_length=1024,)
    genres = models.ManyToManyField(Genre, through='TrackGenres')
    upload_date = models.DateField(auto_now_add=True,)
    audio_file = models.FileField(upload_to='music/files/',)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['-upload_date',]


class TrackGenres(models.Model):
    track = models.ForeignKey(Track, on_delete=models.CASCADE, related_name='genrestotrack')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id',]
        constraints = [
            models.UniqueConstraint(
                fields=['track', 'genre'],
                name='genretotrack_unique'
            )
        ]


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    track = models.ForeignKey(Track, on_delete=models.CASCADE, related_name='likes')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'track'],
                name='userliketrack_unique'
            )
        ]
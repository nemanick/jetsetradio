from django.forms import ModelForm
from users.forms import CommentForm
from music.models import MusicComment, Music


class MusicCreateForm(ModelForm):
    class Meta:
        model = Music
        fields = ['title', 'thumbnail', 'album', 'genres', 'song', 'lyrics']

    def save(self, commit=True):
        instance = super(Music, self).save(commit=False)
        if commit:
            instance.save()
        return instance


class MusicCommentForm(CommentForm):
    class Meta:
        model = MusicComment
        fields = ['body']

        labels = {
            'body': 'Add a comment'
        }

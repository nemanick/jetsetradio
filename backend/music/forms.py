from django.forms import ModelForm, SelectMultiple, FileInput
from users.forms import CommentForm
from music.models import MusicComment, Music


class MusicCreateForm(ModelForm):
    class Meta:
        model = Music
        fields = ['title', 'thumbnail', 'genres', 'song', 'lyrics']
        widgets = {
            'genres': SelectMultiple(attrs={'class': 'cart__amount'}),
            'thumbnail': FileInput(attrs={'type': 'file',
                                          'name': 'thum bnail',
                                          'accept': 'image/*',
                                          'class': 'form-control',
                                          'id': 'id_thumbnail', }),
            'song': FileInput(attrs={'type': 'file',
                                     'name': 'song',
                                     'accept': 'audio/*',
                                     'class': 'form-control',
                                     'id': 'id_song', })
        }

    def __init__(self, *args, **kwargs):
        super(MusicCreateForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({'class': 'sign__input'})
        self.fields['thumbnail'].widget.attrs.update({'class': 'cart__amount'})
        self.fields['song'].widget.attrs.update({'class': 'cart__amount'})
        self.fields['lyrics'].widget.attrs.update({'class': 'sign__textarea'})


class MusicCommentForm(CommentForm):
    class Meta:
        model = MusicComment
        fields = ['body']

        labels = {
            'body': 'Add a comment'
        }

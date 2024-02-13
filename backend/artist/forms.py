from django.forms import ModelForm, FileInput, ValidationError
from django.contrib.auth import get_user_model


class CustomUserEditFrom(ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['picture', 'username', 'bio']
        widgets = {'picture': FileInput(attrs={'type': 'file',
                                               'name': 'picture',
                                               'accept': 'image/*',
                                               'class': 'form-control',
                                               'id': 'id_picture', })}

    def __init__(self, *args, **kwargs):
        super(CustomUserEditFrom, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({'class': 'sign__input'})
        self.fields['picture'].widget.attrs.update({'class': 'cart__amount'})
        self.fields['bio'].widget.attrs.update({'class': 'sign__textarea'})

    def clean_picture(self):
        picture = self.cleaned_data['picture']
        if picture:
            file_extension = picture.name.split('.')[-1].lower()
            if file_extension not in ['jpg', 'jpeg', 'png', 'gif']:
                raise ValidationError('Only images (JPEG, PNG, GIF)'
                                      ' are allowed.')

            return picture
        else:
            return None

from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets

from webapp.models import Photo, Album


class PhotoForm(forms.ModelForm):
    album = forms.ModelChoiceField(queryset=Album.objects.all())

    def __init__(self, *args, **kwargs):
        user = kwargs['initial'].pop('user', None)
        super(PhotoForm, self).__init__(*args, **kwargs)

        if user:
            self.fields['album'].queryset = Album.objects.filter(user=user)

    class Meta:
        model = Photo
        exclude = ['id', 'is_created', 'user']


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['name', "description", 'is_private']
        widgets = {
            "description": widgets.Textarea(attrs={"placeholder": "Введите описание"})
        }


class PhotoDeleteForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ["id"]


class AlbumDeleteForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ["id"]

from django import forms
from django.forms import formset_factory
#from discovbeat.models import UserPlaylist,Song

class PlaylistShareForm(forms.Form):
    playlist_description = forms.CharField(widget=forms.Textarea,label="Description", max_length=1000, required=False)
    shareduser = forms.CharField(label="Who do you want to share this with?", max_length=500, required=True)

class SongShareForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea, label="Write you description about the song!", max_length=1000, required=False)

    # # Formset Allows for adding multiple forms
    # songShareFormset = formset_factory(SongShareForm)
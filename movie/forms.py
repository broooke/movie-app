from django import forms
from movie.models import Movie


class createMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        exclude = ('user',)
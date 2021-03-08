from django import forms
from movie.models import Movie, Reviews

class createMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        exclude = ('user',)

class addReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ('email', 'name', 'text',)

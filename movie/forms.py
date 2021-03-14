from django import forms
from movie.models import Movie, Reviews, Rating, RatingStar


class createMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        exclude = ('user',)

class addReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ('email', 'name', 'text',)

class RatingForm(forms.ModelForm):
    star = forms.ModelChoiceField(
        queryset=RatingStar.objects.all(), widget=forms.RadioSelect(), empty_label=None
    )

    class Meta:
        model = Rating
        fields = ("star",)

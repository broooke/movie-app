import django_filters

class MovieFilter(django_filters.FilterSet):
    class Meta:
        model = Movie
        fields = '__all__'
        exclude = ['user',]

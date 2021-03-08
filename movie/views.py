from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

from movie.forms import createMovieForm, addReviewForm
from movie.models import Movie, Genre, Actor
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


def homePage(request):
    if request.method == 'POST':
        return redirect('register-user')
    return render(request, 'page/home.html')

def detailsMoviePage(request, pk):
    movie = Movie.objects.get(id=pk)
    movies = Movie.objects.all()
    context = {'movie':movie, 'movies':movies}
    return render(request, 'django_movie/moviesingle.html', context)

def createMovie(request):
    form = createMovieForm()
    if request.method == 'POST':
        form = createMovieForm(request.POST, request.FILES)
        if form.is_valid():
            form_save = form.save(commit=False)
            form_save.user = request.user
            form_save.save()
            return redirect('list-movies')

    context = {'form':form}
    return render(request, 'page/MovieDetails.html', context)

def updateMovie(request, pk):
    movie = Movie.objects.get(id=pk)
    form = createMovieForm(instance=movie)
    if request.method == 'POST':
        form = createMovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
             form.save()
             return redirect('list-movies')
    context = {'form':form}
    return render(request, 'page/MovieDetails.html', context)

def deleteMovie(request, pk):
    movie = Movie.objects.get(id=pk)
    movie.delete()
    return redirect('list-movies')

def listMoviePage(request):
    movies = Movie.objects.all()
    genres = Genre.objects.all()
    years = getYears()
    if 'year' in request.GET:
        movies = Movie.objects.filter(Q(year__in=request.GET.getlist("year")) | Q(genres__in=request.GET.getlist("genre")))
    context = {'movies': movies, 'genres':genres, 'years': set(years)}
    return render(request, 'django_movie/movies.html', context)

def getYears():
    years = Movie.objects.all().values_list("year")
    return years

def addReview(request, pk):
    if request.method == 'POST':
        form = addReviewForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get('parent'))
            form.movie_id = pk
            form.save()
            return redirect('list-movies')
    else:
        return HttpResponse('Error')

def actorsPage(request, name):
    actor = Actor.objects.get(name=name)
    movies = Movie.objects.all()
    genres = Genre.objects.all()
    context = {'actor':actor, 'movies':movies, 'genres':genres}
    return render(request, 'django_movie/acters.html', context)



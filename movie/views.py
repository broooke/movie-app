from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from movie.forms import createMovieForm
from movie.models import Movie
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


def homePage(request):
    if request.method == 'POST':
        return redirect('register-user')
    return render(request, 'page/home.html')

def detailsMoviePage(request, pk):
    movie = Movie.objects.get(id=pk)
    context = {'movie':movie}
    return render(request, 'page/MovieDetails.html', context)

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
    context = {'movies': movies}
    return render(request, 'githubPage/index.html', context)




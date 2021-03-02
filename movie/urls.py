from django.urls import path, include

from movie import views

urlpatterns = [
    path('list/', views.getMovies, name='list-movies'),
    path('list/<str:pk>/', views.getMovie, name='details-movie'),
    path('create/', views.createMovie, name='create-movie'),
    path('update/<str:pk>/', views.updateMovie, name='update-movie'),
    path('delete/<str:pk>/', views.deleteMovie, name='delete-movie'),
]
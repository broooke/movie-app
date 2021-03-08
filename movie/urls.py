from django.urls import path, include

from movie import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('list/<str:pk>/', views.detailsMoviePage, name='details-movie'),
    path('create/', views.createMovie, name='create-movie'),
    path('update/<str:pk>/', views.updateMovie, name='update-movie'),
    path('delete/<str:pk>/', views.deleteMovie, name='delete-movie'),
    path('home/', views.listMoviePage, name='list-movies'),
    path('add_review/<str:pk>/', views.addReview, name='add-review'),
    path('actor/<str:name>/', views.actorsPage, name='actors'),
]
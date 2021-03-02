from django.urls import path, include

from authorization import views

urlpatterns = [
    path('login/', views.loginUser, name='login-user'),
    path('signup/', views.signupUser, name='signup-user'),
]
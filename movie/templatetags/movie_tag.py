from django import template
from movie.models import Category, Movie

register = template.Library()

@register.simple_tag()
def get_categories():
    return Category.objects.all()

@register.simple_tag()
def get_last_movies():
    return Movie.objects.order_by("id")[:3]
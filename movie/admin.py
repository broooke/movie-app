from django.contrib import admin
from movie.models import *

admin.site.register(Movie)
admin.site.register(Category)
admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(MovieShots)
admin.site.register(RatingStar)
admin.site.register(Rating)
admin.site.register(Reviews)


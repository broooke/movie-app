from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse


class Movie(models.Model):
    """Фильм"""
    title = models.CharField("Название", max_length=100, null=True)
    tagline = models.CharField("Слоган", max_length=100, default='', null=True)
    description = models.TextField("Описание" , null=True)
    poster = models.ImageField("Постер", upload_to="movies/", null=True, default='placeholder.png')
    year = models.PositiveSmallIntegerField("Дата выхода", default=2019 , null=True)
    country = models.CharField("Страна", max_length=30, null=True)
    # directors = models.ManyToManyField(Actor, verbose_name="режиссер", related_name="film_director")
    # actors = models.ManyToManyField(Actor, verbose_name="актеры", related_name="film_actor")
    # genres = models.ManyToManyField(Genre, verbose_name="жанры")
    # world_premiere = models.DateField("Примьера в мире", default=date.today)
    budget = models.PositiveIntegerField("Бюджет", default=0,
                                         help_text="указывать сумму в долларах", null=True)
    fees_in_usa = models.PositiveIntegerField(
        "Сборы в США", default=0, help_text="указывать сумму в долларах", null=True
    )
    fess_in_world = models.PositiveIntegerField(
        "Сборы в мире", default=0, help_text="указывать сумму в долларах", null=True
    )
    # category = models.ForeignKey(
    #     Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True
    # )
    url = models.SlugField(max_length=130, unique=True, null=True)
    draft = models.BooleanField("Черновик", default=False, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("movie_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"
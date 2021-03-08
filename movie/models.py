from datetime import date

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse

class Category(models.Model):
    """Категории"""
    name = models.CharField("Категория", max_length=150, null=True)
    description = models.TextField("Описание", null=True)
    url = models.SlugField(max_length=160, unique=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Actor(models.Model):
    """Актеры и режиссеры"""
    name = models.CharField("Имя", max_length=100, null=True)
    age = models.PositiveSmallIntegerField("Возраст", default=0, null=True)
    description = models.TextField("Описание", null=True)
    image = models.ImageField("Изображение", upload_to="actors/", null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('actor_detail', kwargs={"slug": self.name})

    class Meta:
        verbose_name = "Актеры и режиссеры"
        verbose_name_plural = "Актеры и режиссеры"


class Genre(models.Model):
    """Жанры"""
    name = models.CharField("Имя", max_length=100, null=True)
    description = models.TextField("Описание", null=True)
    url = models.SlugField(max_length=160, unique=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Movie(models.Model):
    """Фильм"""
    title = models.CharField("Название", max_length=100, null=True)
    tagline = models.CharField("Слоган", max_length=100, default='', null=True, blank=True)
    description = models.TextField("Описание" , null=True)
    poster = models.ImageField("Постер", upload_to="movies/", null=True)
    year = models.PositiveSmallIntegerField("Дата выхода", default=2019 , null=True)
    country = models.CharField("Страна", max_length=30, null=True)
    directors = models.ManyToManyField(Actor, verbose_name="режиссер", related_name="film_director", null=True, blank=True)
    actors = models.ManyToManyField(Actor, verbose_name="актеры", related_name="film_actor", null=True, blank=True)
    genres = models.ManyToManyField(Genre, verbose_name="жанры", null=True, blank=True)
    world_premiere = models.DateField("Примьера в мире", default=date.today)
    budget = models.PositiveIntegerField("Бюджет", default=0,
                                         help_text="указывать сумму в долларах", null=True)
    fees_in_usa = models.PositiveIntegerField(
        "Сборы в США", default=0, help_text="указывать сумму в долларах", null=True
    )
    fess_in_world = models.PositiveIntegerField(
        "Сборы в мире", default=0, help_text="указывать сумму в долларах", null=True
    )
    category = models.ForeignKey(
        Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True, blank=True
    )
    url = models.SlugField(max_length=130, unique=True, null=True)
    draft = models.BooleanField("Черновик", default=False, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("movie_detail", kwargs={"slug": self.url})

    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"


class MovieShots(models.Model):
    """Кадры из фильма"""
    title = models.CharField("Заголовок", max_length=100, null=True)
    description = models.TextField("Описание", null=True)
    image = models.ImageField("Изображение", upload_to="movie_shots/", null=True)
    movie = models.ForeignKey(Movie, verbose_name="Фильм", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Кадр из фильма"
        verbose_name_plural = "Кадры из фильма"


class RatingStar(models.Model):
    """Звезда рейтинга"""
    value = models.SmallIntegerField("Значение", default=0, null=True)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"
        ordering = ["-value"]


class Rating(models.Model):
    """Рейтинг"""
    ip = models.CharField("IP адрес", max_length=15, null=True)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="звезда", null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="фильм", related_name="ratings", null=True)

    def __str__(self):
        return f"{self.star} - {self.movie}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"


class Reviews(models.Model):
    """Отзывы"""
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100, null=True)
    text = models.TextField("Сообщение", max_length=5000, null=True)
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True
    )
    movie = models.ForeignKey(Movie, verbose_name="фильм", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.name} - {self.movie}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"



from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from movies.models import Movie

class Review(models.Model):
  movie = models.ForeignKey('movies.Movie', on_delete=models.PROTECT, related_name='reviews')
  rating = models.IntegerField(validators=[MinValueValidator(1, 'Avaliação não pode ser inferior a 1 estrela'), MaxValueValidator(5, 'Avaliação não pode ser superior a 5 estrela')])
  comment = models.TextField(null=True, blank=True)

  def __str__(self):
    return self.movie.title
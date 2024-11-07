from django.db.models import Avg
from rest_framework import serializers
from movies.models import Movie
from genres.models import Genre
from genres.serializers import GenreSerializer
from actors.models import Actor
from actors.serializers import ActorSerializer


class MovieSerializer(serializers.Serializer):
    title = serializers.CharField()
    genre = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all())
    release_date = serializers.DateField()
    actors = serializers.PrimaryKeyRelatedField(queryset=Actor.objects.all(), many=True)
    sinopse = serializers.CharField()


class MovieModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

    # def get_rate(self, obj):
    #   reviews = obj.reviews.all()

    #   if reviews:
    #     sum_reviews = 0

    #     for review in reviews:
    #       sum_reviews += review.rating
    #     reviews_count = reviews.count()

    #     return round(sum_reviews / len(reviews), 1)
    #   return None

    def validate_release_date(self, value):
        if value.year < 1800:
            raise serializers.ValidationError('A data de lançamento não poder ser anterior a 1990')
        return value

    def validate_sinopse(self, value):
        if len(value) > 500:
            raise serializers.ValidationError('A sinopse deve ter no máximo 200 caracteres')
        return value


class MovieListDetailSerializer(serializers.ModelSerializer):
  actors = ActorSerializer(many=True)
  genre = GenreSerializer()
  rate = serializers.SerializerMethodField(read_only=True)

  class Meta:
    model = Movie
    fields = ['id', 'title', 'genre', 'actors', 'release_date', 'sinopse', 'rate']

    def get_rate(self, obj):
      rate = obj.reviews.aggregate(Avg('rating'))['rating__avg']
      if rate:
        return round(rate, 1)
      return None

from rest_framework import serializers
from movies.models import Movie
from genres.models import Genre
from actors.models import Actor

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
  
  def validate_release_date(self, value):
    if value.year < 1990:
      raise serializers.ValidationError('A data de lançamento não poder ser anterior a 1990')
    return value
  
  def validate_sinopse(self, value):
    if len(value) > 200:
      raise serializers.ValidationError('A sinopse deve ter no máximo 200 caracteres')
    return value
from rest_framework import generics
from movies.models import Movie
from movies.serializes import MovieModelSerializer, MovieSerializer

class MovieCreateListView(generics.ListCreateAPIView):
  queryset = Movie.objects.all()
  serializer_class = MovieModelSerializer

class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Movie.objects.all()
  serializer_class = MovieModelSerializer  
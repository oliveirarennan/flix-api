from rest_framework import generics
from movies.models import Movie
from movies.serializes import MovieModelSerializer, MovieSerializer
from rest_framework.permissions import IsAuthenticated

class MovieCreateListView(generics.ListCreateAPIView):
  permission_classes = (IsAuthenticated,)
  queryset = Movie.objects.all()
  serializer_class = MovieModelSerializer

class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = (IsAuthenticated,)
  queryset = Movie.objects.all()
  serializer_class = MovieModelSerializer  
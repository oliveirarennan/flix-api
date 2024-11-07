from django.db.models import Count, Avg
from rest_framework import generics, views, response, status
from movies.models import Movie
from movies.serializers import MovieModelSerializer, MovieSerializer, MovieListDetailSerializer
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from reviews.models import Review

class MovieCreateListView(generics.ListCreateAPIView):
  permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
  queryset = Movie.objects.all()

  def get_serializer_class(self):
      if self.request.method == 'GET':
        return MovieListDetailSerializer
      return MovieModelSerializer

class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
  queryset = Movie.objects.all()
  
  def get_serializer_class(self):
      if self.request.method == 'GET':
        return MovieListDetailSerializer
      return MovieModelSerializer


class MovieStatsView(views.APIView):
  permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
  queryset = Movie.objects.all()
  def get(self, request):
    total_movies = self.queryset.count()
    movies_by_genre = self.queryset.values('genre__name').annotate(count=Count('id'))
    total_reviews = Review.objects.count()
    average_rating = Review.objects.aggregate(average_rating=Avg('rating'))['avg_rating']

    return response.Response(
      data={
        'total_movies': total_movies,
        'movies_by_genre': movies_by_genre,
        'total_reviews': total_reviews,
        'average_rating': round(average_rating, 1) if average_rating else 0
      },
      status=status.HTTP_200_OK
    )
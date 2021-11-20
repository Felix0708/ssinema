from typing import ContextManager
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated

from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth import get_user_model

from movies.models import Genre, Movie
from movies.serializers import MovieSerializer
from .moviedummy import TMDBHelper
from .movieweather import weatherHelper

from django.db.models import Q
from collections import Counter

# Create your views here.
@api_view(['GET'])
@permission_classes([AllowAny])
def random_movie(request):
    random_movie = Movie.objects.exclude(Q(video_path__isnull=True) | Q(video_path__exact='')).order_by('?')[0]
    random_serializer = MovieSerializer(random_movie)
    
    return Response({"random_movie": random_serializer.data})


@api_view(['GET'])
@permission_classes([AllowAny])
def latest_movies(request):
    # DB 업데이트
    TMDBHelper().create_movies()

    latest_movies = Movie.objects.order_by('release_date').reverse()[:50]
    latest_serializer = MovieSerializer(latest_movies, many=True)

    return Response({"latest_movies": latest_serializer.data})

@api_view(['GET'])
@permission_classes([AllowAny])
def toprate_movies(request):
    toprate_movies = Movie.objects.order_by('vote_average').reverse()[:50]
    toprate_serializer = MovieSerializer(toprate_movies, many=True)

    return Response({"toprate_movies": toprate_serializer.data})


@api_view(['GET'])
@permission_classes([AllowAny])
def mostpop_movies(request):
    mostpop_movies = Movie.objects.order_by('popularity').reverse()[:50]
    mostpop_serializer = MovieSerializer(mostpop_movies, many=True)

    return Response({"mostpop_movies": mostpop_serializer.data,})


@api_view(['GET'])
@permission_classes([AllowAny])
def foruser_movies(request):

    like_movies = Movie.objects.filter(like_users=request.user.pk)

    genre_list = []
    for movie in like_movies:
        genre_list += Movie.objects.filter(pk=movie.pk).values_list('genres', flat=True)
    best_genre_pk = Counter(genre_list).most_common(1)[0][0]
    second_genre_pk = Counter(genre_list).most_common(2)[0][0]

    best_genre_movies = Movie.objects.filter(Q(genres=best_genre_pk) | Q(genres=second_genre_pk))[:50]
    best_genre_serializer = MovieSerializer(best_genre_movies, many=True)

    return Response({"best_genre_movies": best_genre_serializer.data})


@api_view(['GET'])
@permission_classes([AllowAny])
def weather_movies(request):
    weather_movies = weatherHelper().movieRecommendByWeather()
    weather_serializer = MovieSerializer(weather_movies, many=True)

    return Response({"weather_movies": weather_serializer.data})



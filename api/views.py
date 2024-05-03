from django.shortcuts import render
from app.models import Movie
from  .serializer import ModelSerializer,MovieDetailSerializer,MovieSerializer
from rest_framework.views import    Response
from rest_framework.generics import ListAPIView,RetrieveAPIView
# Create your views here.
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter
# Create your views here.
class MovieListAPIView(ListAPIView):
    queryset =Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = (SearchFilter,)
    search_fields=("name",)
class MovieDatailRetrieveAPIView(RetrieveAPIView):
   queryset = Movie.objects.all()
   serializer_class = MovieDetailSerializer
   lookup_field = "pk"

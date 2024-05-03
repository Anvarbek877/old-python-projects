from django.urls import path
from .views import MovieListAPIView,MovieDatailRetrieveAPIView
urlpatterns = [
    path("movie1/",MovieListAPIView.as_view()),
    path("movie2/<int:pk>",MovieDatailRetrieveAPIView.as_view()),






]

from django.urls import path, include
from . import views

urlpatterns = [
    path('movies/', views.MovieList.as_view(), name='movie-list'),
    path('movies/<int:pk>/', views.MovieDetail.as_view(), name='movie-detail'),
    path('showtimes/', views.ShowtimeList.as_view(), name='showtime-list'),
    path('showtimes/<int:pk>/', views.ShowtimeDetail.as_view(), name='showtime-detail'),
    path('bookings/', views.BookingList.as_view(), name='booking-list'),
    path('bookings/<int:pk>/', views.BookingDetail.as_view(), name='booking-detail'),
]
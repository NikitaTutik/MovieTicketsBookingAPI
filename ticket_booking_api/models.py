from django.db import models
from authentication.models import User

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class Showtime(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    available_seats = models.IntegerField()

    def __str__(self):
        return f"Movie: {self.movie}; Time: {self.start_time}"

class Booking(models.Model):
    showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE)
    customer_name = models.ForeignKey(User, on_delete=models.CASCADE)
    num_tickets = models.IntegerField()
    seat_number = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"Ticket #{self.pk} - {self.showtime} - Seat: {self.seat_number}"


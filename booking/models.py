from django.db import models
from django.contrib.auth.models import User


class Booking(models.Model):
    """
    Model represents a restaurant 0booking made by a user
    A connection exists between the user and the booked table
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_bookings")
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150, blank=True, null=True)
    date = models.DateField()
    time = models.IntegerField()
    number_of_guests = models.IntegerField()
    date = models.DateField()


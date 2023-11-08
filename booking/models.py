from django.db import models
from django.contrib.auth.models import User


# Provides a list of time options when the user makes bookings

TIME_OPTIONS = (
    ('12:00', '12:00'),
    ('12:30', '12:30'),
    ('13:00', '13:00'),
    ('13:30', '13:30'),
    ('14:00', '14:00'),
    ('14:30', '14:30'),
    ('15:00', '15:00'),
    ('15:30', '15:30'),
    ('16:00', '16:00'),
    ('16:30', '16:30'),
    ('17:00', '17:00'),
    ('17:30', '17:30'),
    ('18:00', '18:00'),
    ('18:30', '18:30'),
    ('19:00', '19:00'),
    ('19:30', '19:30'),
    ('20:00', '20:00'),
)

# Provides options on the number of guests the user can choose when booking
NUMBER_OF_GUESTS = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
)

class Booking(models.Model):
    """
    Model represents a restaurant booking made by a user
    A connection exists between the user and the booked table
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_bookings")
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank=True, null=True)
    date = models.DateField()
    time = models.CharField(max_length=50, choices=TIME_OPTIONS, blank=False)
    number_of_guests = models.CharField(max_length=10, choices=NUMBER_OF_GUESTS)

    def __str__(self):
        return self.name

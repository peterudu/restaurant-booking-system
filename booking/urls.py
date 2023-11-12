from . import views
from django.urls import path


urlpatterns = [
    path("", views.HomePage.as_view(), name="home"),
    path('bookings/', views.BookingView.as_view(), name='bookings'),
    path('menu/', views.Menu.as_view(), name='menu'),
    path('thanks/', views.Thanks.as_view(), name='thanks'),
    path('sign_up/', views.SignUpView.as_view(), name='sign_up'),
    path('my_bookings/', views.ListBookingView.as_view(), name='my_bookings'),
    path('manage_bookings/<booking_id>', views.manage_booking_view, name='manage'),
    path('delete_booking/<booking_id>', views.delete_booking, name='delete'),
]
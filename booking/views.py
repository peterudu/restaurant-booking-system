from django.shortcuts import render
from django.views import generic
from .models import Booking


# Home Page View
class HomePage(generic.TemplateView):
    """ 
    Renders the home page in the browser
    """
    template_name = 'index.html'

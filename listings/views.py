from django.shortcuts import render
from .models import Listing
# Create your views here.

def index(request):
    listings=Listing.objects.all() # Fetching the listings from the db
    context= {
        'listings' : listings # Passing the listings into dictionary
    }
    return render(request, 'listings/listings.html', context) # Passing the dictionary as an argument

def listing(request, listing_id):
    return render(request, 'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html')


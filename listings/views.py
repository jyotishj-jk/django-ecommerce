from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Listing
# Create your views here.

def index(request):
    listings=Listing.objects.order_by('-list_date').filter(is_published=True) # Fetching the listings from the db
    paginator = Paginator(listings, 6) # No. of listings in one page
    page_number = request.GET.get("page")
    paged_listings = paginator.get_page(page_number)
    context= {
        'listings' : paged_listings # Passing the listings into dictionary
    }
    return render(request, 'listings/listings.html', context) # Passing the dictionary as an argument

def listing(request, listing_id):
    return render(request, 'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html')


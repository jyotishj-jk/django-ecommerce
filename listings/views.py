from django.shortcuts import render,get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from listings.choices import bedroom_choices, price_choices, state_choices
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
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing': listing,
    }
    return render(request, 'listings/listing.html', context)

def search(request):
    queryset_list = Listing.objects.order_by('-list_date')
    # Search keywords
    
    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings': queryset_list
    }
    return render(request, 'listings/search.html', context)


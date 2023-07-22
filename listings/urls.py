from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='listings'), #For listings
    path('<int:listing_id>', views.listing, name='listing'), #For singular listings with id
    path('search', views.search, name='search'), #For search in listings
]
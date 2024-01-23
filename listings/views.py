from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import Listing, Source

def get_all_cat_listings_json(request):
    qs = Listing.objects.all()
    data = serialize("json", qs)
    return HttpResponse(data, content_type="application/json")

def get_source_json(request):
    source_url = request.GET.get('url', 'all')
    thatsource = Source.objects.all()
    if source_url != 'all':
        thatsource = Source.objects.filter(url=source_url)

    data = serialize("json", thatsource)
    return HttpResponse(data, content_type="application/json")
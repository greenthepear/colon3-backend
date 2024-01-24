from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse, HttpResponseNotFound
from .models import Listing, Source
from .serializers import *
from rest_framework.renderers import JSONRenderer

def get_all_cat_listings_json(request):
    cat_id = request.GET.get('id', 'all')
    qs = Listing.objects.all()

    if cat_id != 'all':
        try:
            qs = Listing.objects.filter(id=cat_id)
        except:
            return HttpResponseNotFound("Not found.")
        
    data = serialize("json", qs)
    return HttpResponse(data, content_type="application/json")

def get_all_cat_listings_json_full(request):
    cat_id = request.GET.get('id', 'all')
    qs = Listing.objects.all()

    if cat_id != 'all':
        try:
            qs = Listing.objects.filter(id=cat_id)
        except:
            return HttpResponseNotFound("Not found.")
    

    data = JSONRenderer().render(FullCatSerializer(qs, many=True).data)
    return HttpResponse(data, content_type="application/json")

def get_source_json(request):
    source_url = request.GET.get('url', 'all')
    thatsource = Source.objects.all()
    if source_url != 'all':
        thatsource = Source.objects.filter(url=source_url)
        if len(thatsource) == 0:
            return HttpResponseNotFound("Not found.")

    data = serialize("json", thatsource)
    return HttpResponse(data, content_type="application/json")
from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse, HttpResponseNotFound
from .models import Listing, Source
from .serializers import *
from rest_framework.renderers import JSONRenderer


def gen_json_http_response(data):
    res = HttpResponse(serialize("json", data), "application/json")

    res["Access-Control-Allow-Origin"] = "*"
    res["Access-Control-Allow-Methods"] = "GET"
    res["Access-Control-Max-Age"] = "1000"
    res["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"

    return res

def get_all_cat_listings_json(request):
    cat_id = request.GET.get('id', 'all')
    qs = Listing.objects.all()

    if cat_id != 'all':
        try:
            qs = Listing.objects.filter(id=cat_id)
        except:
            return HttpResponseNotFound("Not found.")
        
    return gen_json_http_response(qs)

def get_all_cat_listings_json_full(request):
    cat_id = request.GET.get('id', 'all')
    qs = Listing.objects.all()

    if cat_id != 'all':
        try:
            qs = Listing.objects.filter(id=cat_id)
        except:
            return HttpResponseNotFound("Not found.")
    

    data = JSONRenderer().render(FullCatSerializer(qs, many=True).data)
    res = HttpResponse(data, content_type="application/json")

    res["Access-Control-Allow-Origin"] = "*"
    res["Access-Control-Allow-Methods"] = "GET"
    res["Access-Control-Max-Age"] = "1000"
    res["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"

    return res

def get_source_json(request):
    source_url = request.GET.get('url', 'all')
    thatsource = Source.objects.all()
    if source_url != 'all':
        thatsource = Source.objects.filter(url=source_url)
        if len(thatsource) == 0:
            return HttpResponseNotFound("Not found.")

    return gen_json_http_response(thatsource)
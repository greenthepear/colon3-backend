from django.urls import path

from . import views

urlpatterns = [
    path("", views.get_all_cat_listings_json, name="getAllCatsJson"),
    path("sources", views.get_source_json, name="getSourceInfo")
]
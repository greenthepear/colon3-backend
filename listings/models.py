import uuid
from django.db import models

class Source(models.Model):
    url = models.CharField(max_length=255, primary_key=True)
    full_name = models.CharField(max_length=511)
    city = models.CharField(max_length=127)
    address = models.CharField(max_length=511)

    def __str__(self):
        return self.url

class Listing(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    listing_url = models.CharField(max_length=511)
    cat_name = models.CharField(max_length=127)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=255)
    cat_age = models.IntegerField()
    cat_sex = models.CharField(max_length=5)
    added_date = models.DateTimeField(max_length=200)

    def __str__(self):
        return self.id

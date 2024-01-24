from rest_framework import serializers
from .models import Listing, Source


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = '__all__'
      
class FullCatSerializer(serializers.ModelSerializer):
    source = SourceSerializer(many=False)
    
    class Meta:
        model = Listing
        fields = '__all__'
from rest_framework import serializers
from .models import Song, Artist


class SongSerializer(serializers.ModelSerializer):
    class Meta:
      model = Song
      fields = ('id', 'name')
      
class ArtistSerializer(serialisers.ModelSerializer):
  songs = SongSerializer(many=True)
   
  class Meta:
    model = Artist
    fields = ('id', 'name', 'songs')
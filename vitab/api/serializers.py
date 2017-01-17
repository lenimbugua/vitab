from rest_framework import serializers

from .models import Photo

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'date_added', 'creator', 'image', 'is_public')

from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

from rest_framework import generics

from .models import Photo
from .serializers import PhotoSerializer


class PhotoListView(generics.ListCreateAPIView):
    def get_queryset(self):
        if self.request.user.is_authenticated():
            return Photo.objects.filter(creator=self.request.user)
        else:
            return Photo.objects.filter(is_public=True)

    serializer_class = PhotoSerializer

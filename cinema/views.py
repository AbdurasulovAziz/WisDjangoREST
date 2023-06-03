from django.shortcuts import render
from rest_framework import generics

from cinema.models import Film, Seance
from cinema.serializers import FilmSerializer, SeanceSerializer


# Create your views here.


class FilmPage(generics.ListAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

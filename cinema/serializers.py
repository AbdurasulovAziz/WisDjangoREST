from rest_framework import serializers

from cinema.models import Film, Seance, Genre


class SeanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Seance
        fields = ['id', 'datetime', 'price']


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'


class FilmSerializer(serializers.ModelSerializer):
    genre = serializers.StringRelatedField(many=True)
    seance = SeanceSerializer(many=True)

    class Meta:
        model = Film
        fields = [
            'id',
            'name',
            'description',
            'age_limit',
            'director',
            'trailer',
            'genre',
            'seance'
        ]

        
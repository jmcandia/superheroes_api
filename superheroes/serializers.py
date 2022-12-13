from rest_framework import serializers

from .models import Superhero


class SuperheroSerializer(serializers.Serializer):
    class Meta:
        model = Superhero
        fields = '__all__'

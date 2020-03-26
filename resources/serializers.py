from resources.models import Filme
from django.contrib.auth.models import User
from rest_framework import serializers

class FilmeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filme
        owner = serializers.ReadOnlyField(source='owner.username')
        fields = ['id', 'titulo', 'diretor', 'sinopse', 'genero', 'owner']

class UserSerializer(serializers.ModelSerializer):
    filmes = serializers.PrimaryKeyRelatedField(many=True, queryset=Filme.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'filmes']
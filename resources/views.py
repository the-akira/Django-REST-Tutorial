from resources.models import Filme
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from resources.serializers import FilmeSerializer, UserSerializer
from rest_framework import generics

class FilmeList(generics.ListCreateAPIView):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
	    serializer.save(owner=self.request.user)

class FilmeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer
    permission_classes = [IsAuthenticated]

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
from django.db import models

class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    diretor = models.CharField(max_length=100)
    sinopse = models.TextField()
    genero = models.CharField(max_length=100)
    owner = models.ForeignKey('auth.User', related_name='filmes', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
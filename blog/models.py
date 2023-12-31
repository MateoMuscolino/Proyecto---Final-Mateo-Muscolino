from django.db import models
from django.contrib.auth.models import User

class Opinion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) # El cascade hace que si un usuario elimina, se eliminaran las demas
    libro = models.CharField(max_length=100)
    opinion = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.libro
    